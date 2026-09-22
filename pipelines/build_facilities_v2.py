#!/usr/bin/env python3
"""Atlas pipeline v2 — tiered provenance.

Tier 1 (official registers) supplies identity and attributes:
  - IAEA NFCFDB facility list export   (raw/nfcfdb_facilitylist_20260922.xlsx)
  - IAEA RRDB reactor list export      (raw/rrdb_reactorlist_export_20260922.xlsx)
Tier 2 (published compilations) supplies identity for the fissile/military layer and coordinates:
  - IPFM enrichment / reprocessing map + table CSVs (raw/ipfm_*_20260922.csv)
  - DoD Nuclear Matters Handbook ch. 5 for the U.S. Nuclear Security Enterprise (military/us_nse_sites_dod_nmhb.csv)
  - official pages (ONR, CEA, DOE), IPFM country pages, the Nuclear Notebook and Decree 556 (via Podvig)
    for weapons-program sites outside the U.S. NSE (military/weapons_program_sites_intl.csv)
Tier 3 (crowd-sourced) supplies COORDINATES ONLY, through the reviewed crosswalk:
  - the earlier Wikidata build (public/data/facilities.geojson) as coordinate donor
  - crosswalk/facilities_crosswalk.csv: one row per tier-1 record that has a coordinate donor,
    with reviewed_by blank until a human confirms. Unreviewed rows are drawn with coord_tier=3
    and a distinct marker; tier-1 records with no donor appear in the table without geometry.

No name matching is used to assert identity. The crosswalk PROPOSES matches by exact
normalized name + country; a proposal is a proposal until reviewed.

Outputs:
  public/data/facilities_v2.geojson   (civil: NFCFDB + RRDB; features may lack geometry)
  public/data/facilities_fissile.geojson (enrichment + reprocessing from IPFM, all states, with
                                          civil/military/dual designation as IPFM gives it)
  public/data/facilities_military.geojson (state weapons-program sites: IPFM Military/Dual rows +
                                          DoD-listed U.S. sites; vanilla descriptions only)
  pipelines/build/facilities_v2_report.md
"""
import csv, json, re, unicodedata, datetime, os
from collections import Counter, defaultdict
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RAW = os.path.join(HERE, 'raw')
OUT = os.path.join(ROOT, 'public', 'data')
TODAY = '2026-09-22'

def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).encode('ascii', 'ignore').decode()
    s = s.lower()
    s = re.sub(r'\b(nuclear|power|plant|station|research|reactor|facility|the|of|npp|generating)\b', ' ', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s).strip()
    return re.sub(r'\s+', ' ', s)

COUNTRY_ALIASES = {
    'united states of america': 'united states', 'usa': 'united states', 'us': 'united states',
    'russian federation': 'russia', 'korea, republic of': 'south korea', 'republic of korea': 'south korea',
    'korea, democratic people\'s republic of': 'north korea', 'dprk': 'north korea',
    'iran, islamic republic of': 'iran', 'iran (islamic republic of)': 'iran', 'czechia': 'czech republic',
    'taiwan, china': 'taiwan', 'china, taiwan': 'taiwan', 'viet nam': 'vietnam', 'türkiye': 'turkey', 'turkiye': 'turkey',
    'united kingdom of great britain and northern ireland': 'united kingdom', 'uk': 'united kingdom',
    'people\'s republic of china': 'china', 'syrian arab republic': 'syria', 'bolivia (plurinational state of)': 'bolivia',
}
def ncountry(c):
    c = norm(c); return COUNTRY_ALIASES.get(c, c)

# ---------- tier 1: NFCFDB ----------
STAGE_FROM_TYPE = [
    (r'enrich', 'enrichment'), (r'reprocess', 'reprocessing'), (r'ore processing|mining|milling|in situ|heap', 'mining'),
    (r'conversion', 'conversion'), (r'fuel fabrication|pellet|assembly', 'fabrication'),
    (r'storage|disposal|repository|waste|treatment|conditioning', 'waste'), (r'heavy water', 'heavy-water'),
    (r'zirconium|alloy', 'materials'),
]
def stage_for(t):
    t = (t or '').lower()
    for pat, st in STAGE_FROM_TYPE:
        if re.search(pat, t): return st
    return 'other'

def load_nfcfdb():
    wb = openpyxl.load_workbook(os.path.join(RAW, 'nfcfdb_facilitylist_20260922.xlsx'), read_only=True)
    rows = list(wb.active.iter_rows(values_only=True))
    hi = next(i for i, r in enumerate(rows) if r and 'Facility Name' in [str(x) for x in r])
    hdr = [str(x) for x in rows[hi]]
    out = []
    for r in rows[hi + 1:]:
        d = dict(zip(hdr, r))
        if not d.get('Facility Name'): continue
        out.append({
            'id': 'NFCFDB:' + norm(d['Country']) + ':' + norm(d['Facility Name']),
            'name': str(d['Facility Name']).strip(), 'country': str(d['Country']).strip(),
            'stage': stage_for(d.get('Facility Type')), 'subtype': d.get('Facility Type'),
            'fuel_type': d.get('Fuel Type') or None, 'status': d.get('Facility Status'), 'scale': d.get('Scale'),
            'capacity': d.get('Design Capacity'), 'start': d.get('Start of Operation'), 'end': d.get('End of Operation'),
            'prov': [{'tier': 1, 'source': 'IAEA NFCFDB facility list export', 'record': str(d['Facility Name']).strip(),
                      'url': 'https://infcis.iaea.org/NFCFDB/Facilities', 'retrieved': TODAY}],
        })
    return out

# ---------- tier 1: RRDB ----------
def load_rrdb():
    wb = openpyxl.load_workbook(os.path.join(RAW, 'rrdb_reactorlist_export_20260922.xlsx'), read_only=True)
    rows = list(wb.active.iter_rows(values_only=True))
    hi = next(i for i, r in enumerate(rows) if r and 'Facility Name' in [str(x) for x in r])
    hdr = [str(x) for x in rows[hi]]
    # the JSON API export carries the IAEA code; join on facName+country to it (both are the same register)
    api = json.load(open(os.path.join(RAW, 'rrdb_reactorlist_20260922.json')))['data']
    code = {(norm(a['facName']), ncountry(a['country'])): a['iaeaCode'] for a in api}
    out = []
    for r in rows[hi + 1:]:
        d = dict(zip(hdr, r))
        if not d.get('Facility Name'): continue
        k = (norm(d['Facility Name']), ncountry(d['Country']))
        out.append({
            'id': 'RRDB:' + (code.get(k) or k[0] + ':' + k[1]), 'name': str(d['Facility Name']).strip(), 'country': str(d['Country']).strip(),
            'stage': 'reactor-research', 'subtype': d.get('Type'), 'city': d.get('City'),
            'thermal_power_kw': d.get('Thermal Power'), 'status': d.get('Status'), 'start': (str(d.get('First Criticality Date') or '')[:10] or None),
            'prov': [{'tier': 1, 'source': 'IAEA Research Reactor Database export', 'record': code.get(k) or str(d['Facility Name']).strip(),
                      'url': 'https://nucleus.iaea.org/rrdb/', 'retrieved': TODAY}],
        })
    return out

# ---------- tier 3 donor + crosswalk ----------
def load_donor():
    d = json.load(open(os.path.join(OUT, 'facilities.geojson')))
    donor = defaultdict(list)
    for f in d['features']:
        p = f['properties']; donor[(norm(p['name']), ncountry(p.get('country')))].append((p['id'], f['geometry']['coordinates']))
    return donor

def load_or_build_crosswalk(tier1, donor):
    path = os.path.join(HERE, 'crosswalk', 'facilities_crosswalk.csv')
    existing = {}
    if os.path.exists(path):
        for r in csv.DictReader(open(path)): existing[r['tier1_id']] = r
    rows = []
    for rec in tier1:
        k = (norm(rec['name']), ncountry(rec['country']))
        prev = existing.get(rec['id'])
        if prev: rows.append(prev); continue
        cands = donor.get(k, [])
        if len(cands) == 1:
            qid, (lon, lat) = cands[0]
            rows.append({'tier1_id': rec['id'], 'name': rec['name'], 'country': rec['country'], 'donor': 'wikidata', 'donor_id': qid,
                         'lat': lat, 'lon': lon, 'proposed_by': 'exact-name-country', 'reviewed_by': '', 'reviewed_on': '', 'note': ''})
        else:
            rows.append({'tier1_id': rec['id'], 'name': rec['name'], 'country': rec['country'], 'donor': '', 'donor_id': '',
                         'lat': '', 'lon': '', 'proposed_by': '', 'reviewed_by': '', 'reviewed_on': '', 'note': ('ambiguous: %d candidates' % len(cands)) if cands else 'no donor'})
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['tier1_id', 'name', 'country', 'donor', 'donor_id', 'lat', 'lon', 'proposed_by', 'reviewed_by', 'reviewed_on', 'note'])
        w.writeheader(); w.writerows(rows)
    return {r['tier1_id']: r for r in rows}

def feature(rec, coord, coord_tier, coord_src):
    props = {k: v for k, v in rec.items() if k != 'prov'}
    props['prov'] = rec['prov']
    props['coord_tier'] = coord_tier; props['coord_source'] = coord_src
    geom = {'type': 'Point', 'coordinates': [float(coord[1]), float(coord[0])]} if coord else None
    return {'type': 'Feature', 'geometry': geom, 'properties': props}

# ---------- tier 2: IPFM fissile layer ----------
def load_ipfm(kind):
    maprows = list(csv.DictReader(open(os.path.join(RAW, f'ipfm_{kind}_map_20260922.csv'))))
    tab = list(csv.DictReader(open(os.path.join(RAW, f'ipfm_{kind}_table_20260922.csv'))))
    ALIAS = {'rattehalli': 'ratehalli', 'dimona': 'dimona', 'mayak': 'rt 1', 'zheleznogorsk': 'edc', 'savannah river site': 'h canyon', 'jinta': 'jinta project i ii'}
    def tkey(s):
        k = norm(s.split('(')[0].split(',')[0]); return ALIAS.get(k, k)
    tab_by = {}
    for t in tab: tab_by.setdefault(tkey(t['facility']), []).append(t)
    feats = []
    for m in maprows:
        label = m['label']; lab2 = m.get('label2', '')
        site = label if not re.match(r'^(URENCO|American Centrifuge Plant)$', label) else (lab2.split(',')[0] if lab2 else label)
        site = site.split(',')[0].strip()
        cands = tab_by.get(tkey(site), [])
        if not cands and lab2: cands = tab_by.get(tkey(lab2), [])
        if not cands:
            for k2, v in tab_by.items():
                if k2 and (k2 in norm(site) or norm(site) in k2): cands = v; break
        t = cands[0] if cands else {}
        feats.append({'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [float(m['longitude']), float(m['latitude'])]},
            'properties': {'id': f'IPFM:{kind}:{norm(m["name"])}:{norm(site)}', 'name': site, 'country': m['name'],
                'stage': 'enrichment' if kind == 'enrichment' else 'reprocessing', 'designation': t.get('type', 'unlisted'),
                'status': t.get('status'), 'safeguards': t.get('safeguards'), 'capacity': t.get('capacity_tSWU') or t.get('capacity_tHM'),
                'capacity_unit': 'tSWU/yr' if kind == 'enrichment' else 'tHM/yr', 'coord_tier': 2, 'coord_source': 'IPFM map data',
                'prov': [{'tier': 2, 'source': f'IPFM, Facilities: {kind.capitalize()} plants (map and table, as of 2026)',
                          'url': f'https://fissilematerials.org/facilities/{"enrichment_plants" if kind=="enrichment" else "reprocessing_plants"}.html', 'retrieved': TODAY}]}})
    return feats

def load_us_nse():
    look = {r[0]: r for r in json.load(open(os.path.join(HERE, 'crosswalk', '_wikidata_nse_lookup.json')))}
    feats = []
    for r in csv.DictReader(open(os.path.join(HERE, 'military', 'us_nse_sites_dod_nmhb.csv'))):
        w = look.get(r['name'])
        geom = {'type': 'Point', 'coordinates': [w[3], w[2]]} if w else None
        feats.append({'type': 'Feature', 'geometry': geom, 'properties': {
            'id': 'NSE:' + norm(r['name']), 'name': r['name'], 'country': r['country'], 'role': r['role'], 'city': r['city'], 'region': r['region'],
            'description': r['description'], 'stage': 'weapons-program', 'designation': 'Military (state-disclosed)',
            'coord_tier': 3 if w else None, 'coord_source': ('Wikidata ' + w[1]) if w else None,
            'prov': [{'tier': 1, 'source': r['source'], 'url': r['source_url'], 'retrieved': TODAY}]}})
    return feats

def load_intl_weapons():
    """State weapons-program sites outside the U.S. NSE (military/weapons_program_sites_intl.csv).
    Identity from the row's single cited source (official page, IPFM country page, Nuclear Notebook,
    or Decree 556 as compiled by Podvig). Coordinates are tier 3 (Wikidata item, often a city or
    commune centroid — see coord_note) except where the source itself gives one (tier 2)."""
    feats = []
    for r in csv.DictReader(open(os.path.join(HERE, 'military', 'weapons_program_sites_intl.csv'))):
        has = bool(r['lat'])
        geom = {'type': 'Point', 'coordinates': [float(r['lon']), float(r['lat'])]} if has else None
        tier2 = has and not r['coord_qid']
        feats.append({'type': 'Feature', 'geometry': geom, 'properties': {
            'id': 'WP:' + norm(r['name']), 'name': r['name'], 'country': r['country'], 'role': r['role'], 'city': r['city'], 'region': r['region'],
            'status': r['status'], 'description': r['description'], 'stage': 'weapons-program',
            'designation': 'Military (state-disclosed)' if 'Decree' in r['source'] or r['source'].startswith(('Office for Nuclear', 'CEA', 'U.S. Department')) else 'Military (published compilation)',
            'coord_tier': (2 if tier2 else 3) if has else None,
            'coord_source': (r['source'] if tier2 else 'Wikidata ' + r['coord_qid']) if has else None,
            'coord_note': r['coord_note'] or None,
            'prov': [{'tier': 1 if ('Decree' in r['source'] or r['source'].startswith(('Office for Nuclear', 'CEA', 'U.S. Department'))) else 2, 'source': r['source'], 'url': r['source_url'], 'retrieved': TODAY}]}})
    return feats

def main():
    os.makedirs(os.path.join(HERE, 'build'), exist_ok=True)
    nf = load_nfcfdb(); rr = load_rrdb(); tier1 = nf + rr
    donor = load_donor(); xw = load_or_build_crosswalk(tier1, donor)
    feats = []; with_coord = reviewed = 0
    for rec in tier1:
        x = xw.get(rec['id'], {})
        if x.get('lat'):
            with_coord += 1; rv = bool(x.get('reviewed_by')); reviewed += rv
            feats.append(feature(rec, (x['lat'], x['lon']), 3 if not rv else '3r', f"{x['donor']} {x['donor_id']}"))
        else:
            feats.append(feature(rec, None, None, None))
    civil = {'type': 'FeatureCollection', 'name': 'facilities_v2', 'meta': {'built': TODAY, 'tiers': 'identity=1 (IAEA NFCFDB, RRDB); coordinates=3 (Wikidata via crosswalk, r=reviewed)'}, 'features': feats}
    json.dump(civil, open(os.path.join(OUT, 'facilities_v2.geojson'), 'w'), ensure_ascii=False)
    fiss = load_ipfm('enrichment') + load_ipfm('reprocessing')
    json.dump({'type': 'FeatureCollection', 'name': 'facilities_fissile', 'meta': {'built': TODAY, 'source': 'IPFM facility maps and tables, as of 2026; designations as IPFM gives them'}, 'features': fiss},
              open(os.path.join(OUT, 'facilities_fissile.geojson'), 'w'), ensure_ascii=False)
    mil = [f for f in fiss if re.search(r'military|dual|uncertain', (f['properties'].get('designation') or ''), re.I)]
    for f in mil: f = f  # IPFM rows keep their own prov
    mil = [dict(f, properties=dict(f['properties'], stage='weapons-program')) for f in mil] + load_us_nse() + load_intl_weapons()
    json.dump({'type': 'FeatureCollection', 'name': 'facilities_military', 'meta': {'built': TODAY, 'rule': 'only sites named in an official disclosure or a published compilation; one citation per row; plain descriptions; no protection, layout or inventory detail'}, 'features': mil},
              open(os.path.join(OUT, 'facilities_military.geojson'), 'w'), ensure_ascii=False)
    rep = [f'# facilities v2 build report — {TODAY}', '',
           f'- NFCFDB records: {len(nf)} (stages: {dict(Counter(r["stage"] for r in nf))})',
           f'- RRDB records: {len(rr)} (status: {dict(Counter(r["status"] for r in rr).most_common(6))})',
           f'- tier-1 records with a proposed coordinate: {with_coord} of {len(tier1)}; reviewed: {reviewed}',
           f'- fissile layer (IPFM): {len(fiss)} features ({dict(Counter(f["properties"]["designation"] for f in fiss))})',
           f'- military layer: {len(mil)} features ({dict(Counter(f["properties"]["country"] for f in mil))})', '']
    open(os.path.join(HERE, 'build', 'facilities_v2_report.md'), 'w').write('\n'.join(rep)); print('\n'.join(rep))

if __name__ == '__main__':
    main()
