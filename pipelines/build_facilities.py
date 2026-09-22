#!/usr/bin/env python3
"""
build_facilities.py — first-cut civil fuel-cycle facility layer from Wikidata (CC0) →
public/data/facilities.geojson. Every feature carries its Wikidata QID as the source record,
the class it was matched on, and the retrieval date. Coverage is what Wikidata holds: complete
for power stations, partial for research reactors, sparse for other fuel-cycle steps — see
SOURCES.md and the completion tasks in the atlas page.
"""
import json, os, sys, time, datetime, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'public', 'data', 'facilities.geojson')
RAW = os.path.join(HERE, 'raw', f'wikidata_facilities_{datetime.date.today().isoformat()}.json')
UA = 'nuclear.academy atlas pipeline (contact: howardlewishall@gmail.com)'
ENDPOINT = 'https://query.wikidata.org/sparql'

# Wikidata class → fuel-cycle stage
CLASSES = [
    ('Q134447',  'reactor-power',    'nuclear power plant'),
    ('Q1438105', 'reactor-research', 'research reactor'),
    ('Q54360657','enrichment',       'uranium enrichment plant'),
    ('Q64785417','reprocessing',     'nuclear reprocessing site'),
    ('Q28599311','mining',           'uranium mine'),
    ('Q1340555', 'disposal',         'deep geological repository'),
]

QUERY = """
SELECT ?item ?itemLabel ?coord ?countryLabel ?operatorLabel ?inception ?stateLabel ?dissolved ?capacity WHERE {
  ?item wdt:P31 wd:%s ; wdt:P625 ?coord .
  OPTIONAL { ?item wdt:P17 ?country . }
  OPTIONAL { ?item wdt:P137 ?operator . }
  OPTIONAL { ?item wdt:P571 ?inception . }
  OPTIONAL { ?item wdt:P5817 ?state . }
  OPTIONAL { ?item wdt:P576 ?dissolved . }
  OPTIONAL { ?item wdt:P2109 ?capacity . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,[AUTO_LANGUAGE]". }
}
"""

def sparql(q):
    url = ENDPOINT + '?' + urllib.parse.urlencode({'query': q})
    req = urllib.request.Request(url, headers={'Accept': 'application/sparql-results+json', 'User-Agent': UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as r: return json.load(r)
        except Exception as e:
            print('retry', attempt, e, file=sys.stderr); time.sleep(5)
    raise SystemExit('SPARQL failed')

def parse_point(wkt):
    # "Point(lon lat)"
    s = wkt[wkt.index('(') + 1:wkt.index(')')].split()
    return float(s[0]), float(s[1])

features = {}
raw = {}
EXTRA_ITEMS = [('Q757565', 'enrichment', 'uranium enrichment plant')]  # items carried only under the generic class, reclassified by override
for qid, stage, label in CLASSES:
    res = sparql(QUERY % qid)
    rows = res['results']['bindings']
    raw[qid] = rows
    for b in rows:
        item = b['item']['value'].rsplit('/', 1)[1]
        lon, lat = parse_point(b['coord']['value'])
        f = features.get(item)
        props = {
            'id': item, 'name': b.get('itemLabel', {}).get('value', item),
            'stage': stage, 'class': label,
            'country': b.get('countryLabel', {}).get('value'),
            'operator': b.get('operatorLabel', {}).get('value'),
            'first_operation': (b.get('inception', {}).get('value') or '')[:10] or None,
            'status': b.get('stateLabel', {}).get('value'),
            'closed': (b.get('dissolved', {}).get('value') or '')[:10] or None,
            'capacity_mw': float(b['capacity']['value']) if 'capacity' in b else None,
            'source': 'Wikidata', 'source_url': f'https://www.wikidata.org/wiki/{item}',
            'retrieved': datetime.date.today().isoformat(),
        }
        if f is None:
            features[item] = {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [round(lon, 5), round(lat, 5)]}, 'properties': props}
        else:
            # a more specific class wins over 'other'; keep first stage otherwise
            if f['properties']['stage'] == 'other' and stage != 'other': f['properties'].update({'stage': stage, 'class': label})
            for k, v in props.items():
                if f['properties'].get(k) in (None, '') and v not in (None, ''): f['properties'][k] = v
    print(f'{label}: {len(rows)} rows', file=sys.stderr)

for item_q, stage, label in EXTRA_ITEMS:
    res = sparql(QUERY.replace('?item wdt:P31 wd:%s ; wdt:P625 ?coord .', 'BIND(wd:' + item_q + ' AS ?item) ?item wdt:P625 ?coord .') % ())
    for b in res['results']['bindings']:
        lon, lat = parse_point(b['coord']['value'])
        features[item_q] = {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [round(lon, 5), round(lat, 5)]}, 'properties': {
            'id': item_q, 'name': b.get('itemLabel', {}).get('value', item_q), 'stage': stage, 'class': label,
            'country': b.get('countryLabel', {}).get('value'), 'operator': b.get('operatorLabel', {}).get('value'),
            'first_operation': (b.get('inception', {}).get('value') or '')[:10] or None, 'status': b.get('stateLabel', {}).get('value'),
            'closed': (b.get('dissolved', {}).get('value') or '')[:10] or None, 'capacity_mw': None,
            'source': 'Wikidata', 'source_url': f'https://www.wikidata.org/wiki/{item_q}', 'retrieved': datetime.date.today().isoformat()}}
# overrides with reasons (hand corrections never go in the generated file)
ov_path = os.path.join(HERE, 'overrides', 'facilities.json')
if os.path.exists(ov_path):
    for o in json.load(open(ov_path)):
        if o['id'] in features and 'reason' in o:
            if o.get('exclude'): del features[o['id']]; continue
            features[o['id']]['properties'].update({k: v for k, v in o.items() if k not in ('id', 'reason')})
            features[o['id']]['properties']['override_reason'] = o['reason']

os.makedirs(os.path.dirname(RAW), exist_ok=True)
json.dump(raw, open(RAW, 'w'))
fc = {'type': 'FeatureCollection',
      'meta': {'source': 'Wikidata (CC0)', 'retrieved': datetime.date.today().isoformat(), 'classes': [c[2] for c in CLASSES],
               'coverage_note': 'Civil layer only. Complete for nuclear power plants as Wikidata holds them; partial for research reactors; sparse for enrichment, reprocessing, mining, disposal. The generic Wikidata class nuclear facility is deliberately not used (it mixes in defense-program sites). IAEA PRIS/RRDB/NFCIS reconciliation is a listed completion task.',
               'builder': 'pipelines/build_facilities.py'},
      'features': sorted(features.values(), key=lambda f: (f['properties']['stage'], f['properties']['name']))}
json.dump(fc, open(OUT, 'w'), separators=(',', ':'))
from collections import Counter
print('stages:', Counter(f['properties']['stage'] for f in fc['features']), file=sys.stderr)
print(f'wrote {OUT}: {len(fc["features"])} features, {os.path.getsize(OUT)/1e3:.0f} kB', file=sys.stderr)
