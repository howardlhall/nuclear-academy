#!/usr/bin/env python3
"""
build_nuclides.py — ENSDF → src/data/nuclides.json for the nuclear.academy decay-chain calculator.

Source: the NNDC ENSDF distribution unpacked at raw/ensdf_<dist>/ensdf.001 … ensdf.300
(see SOURCES.md for the file, DOI, hash and retrieval date).

What it reads (ENSDF 80-column format, ENSDF Manual, BNL-NCS-51655):
  * "ADOPTED LEVELS[, GAMMAS]" datasets: for the ground state and every level that is metastable
    kept only when its half-life is >= ISOMER_MIN_SEC (1 s; shorter isomers are folded into the ground state), the
    half-life (cols 40-49 value, 50-55 uncertainty/limit) and the continuation-record branches
    %A, %B-, %EC, %B+, %EC+%B+, %IT, %SF, %B-N, %ECP, %P, %N, %2B-, ... .
  * Decay datasets ("<parent> B- DECAY", "EC DECAY", "B+ DECAY", "A DECAY", "IT DECAY") of every
    parent level kept: to split a branch between the daughter's ground state and its isomer(s) by
    intensity balance — population of a daughter level = direct feeding (IB/IE/IA, normalized by
    NB/NR and BR) + total intensity of gammas into it (TI, else RI·(1+CC)) − gammas out. The
    fraction of decays ending in an isomer is the net population of that isomer level.
    Where a decay dataset cannot be balanced (no normalization, no intensities) the whole branch
    is assigned to the daughter ground state and the entry is flagged "isomer_feeding": "unresolved".

Output: src/data/nuclides.json — {meta, nuclides:{key:{...}}}, key = "Tc-99", "Tc-99m", "Pa-234m".
Every entry carries dsid, evaluators, cut-off and edit dates from the dataset header.
"""
import glob, json, math, os, re, sys, datetime, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = sys.argv[1] if len(sys.argv) > 1 else 'ensdf_260901'
RAW = os.path.join(ROOT, 'raw', DIST)
OUT = os.path.join(ROOT, '..', 'public', 'data', 'nuclides.json')
BUILD = os.path.join(ROOT, 'build'); os.makedirs(BUILD, exist_ok=True)
ISOMER_MIN_SEC = 1.0

ELEMENTS = ['n','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
SYM2Z = {s.upper(): z for z, s in enumerate(ELEMENTS)}
UNIT_SEC = {'Y': 365.25*86400, 'D': 86400, 'H': 3600, 'M': 60, 'S': 1, 'MS': 1e-3, 'US': 1e-6, 'NS': 1e-9, 'PS': 1e-12, 'FS': 1e-15, 'AS': 1e-18}

def nucid_parse(nucid):
    m = re.match(r'\s*(\d{1,3})([A-Z]{1,2})\s*$', nucid.upper())
    if not m: return None
    a, sym = int(m.group(1)), m.group(2)
    if sym not in SYM2Z: return None
    return SYM2Z[sym], a

def key_of(z, a, iso=''):
    return f"{ELEMENTS[z]}-{a}{iso}"

def parse_value(s):
    """ENSDF numeric field: '6.0072', '2.111E+5', '' -> float or None."""
    s = s.strip().replace(' ', '')
    if not s: return None
    try: return float(s)
    except ValueError: return None

def parse_unc(valstr, uncstr):
    """ENSDF uncertainty: integer in last digits of the value; '+12-8' asymmetric; LT/GT/AP/LE/GE/CA/SY limits."""
    v = valstr.strip(); u = uncstr.strip()
    if not u: return None, None
    if u in ('LT','GT','LE','GE','AP','CA','SY','?'): return None, u
    m = re.match(r'\+(\d+)-(\d+)$', u)
    def last_digit_scale(vs):
        vs = vs.upper()
        mant = vs.split('E')[0]; exp = int(vs.split('E')[1]) if 'E' in vs else 0
        dec = len(mant.split('.')[1]) if '.' in mant else 0
        return 10 ** (exp - dec)
    try:
        scale = last_digit_scale(v)
        if m: return (int(m.group(1))*scale, int(m.group(2))*scale), None
        return int(u)*scale, None
    except Exception:
        return None, u

def parse_halflife(field, uncfield):
    f = field.strip()
    if not f: return None
    if f.startswith('STABLE'): return {'stable': True}
    m = re.match(r'([0-9.]+(?:E[+-]?\d+)?)\s*([A-Z]+)$', f.upper())
    if not m: return None
    val, unit = m.group(1), m.group(2)
    if unit not in UNIT_SEC: return None   # width units (EV, KEV, MEV) are not half-lives
    sec = float(val) * UNIT_SEC[unit]
    unc, limit = parse_unc(val, uncfield)
    out = {'value': float(val), 'unit': unit, 'seconds': sec}
    if unc is not None:
        out['unc_seconds'] = (unc[0]*UNIT_SEC[unit], unc[1]*UNIT_SEC[unit]) if isinstance(unc, tuple) else unc*UNIT_SEC[unit]
    if limit: out['limit'] = limit
    return out

BRANCH_RE = re.compile(r'%(2B-|B-2N|B-N|B-A|B-P|B\+P|B\+A|ECP|ECA|EC\+%B\+|EC|B\+|B-|IT|SF|A|P|N|2P|2N|3N)\s*(=|<|>|<=|>=|~|AP|LT|GT|LE|GE)\s*([0-9.]+(?:E[+-]?\d+)?)?\s*([0-9+\-]*)')
MODE_DZ_DA = {'B-': (1,0), '2B-': (2,0), 'B-N': (1,-1), 'B-2N': (1,-2), 'B-A': (-1,-4), 'B-P': (0,-1),
              'EC': (-1,0), 'B+': (-1,0), 'EC+B+': (-1,0), 'ECP': (-2,-1), 'ECA': (-3,-4), 'B+P': (-2,-1), 'B+A': (-3,-4),
              'A': (-2,-4), 'IT': (0,0), 'SF': None, 'P': (-1,-1), '2P': (-2,-2), 'N': (0,-1), '2N': (0,-2), '3N': (0,-3)}

def parse_branches(cont_text):
    """From joined 'L' continuation text: list of {mode, pct, limit, unc}."""
    out = []
    for m in BRANCH_RE.finditer(cont_text):
        mode, op, val, unc = m.group(1), m.group(2), m.group(3), m.group(4)
        if mode == 'EC+%B+': mode = 'EC+B+'
        entry = {'mode': mode}
        if val is not None: entry['pct'] = float(val)
        if op not in ('=',): entry['limit'] = op
        if unc and val is not None:
            u, lim = parse_unc(val, unc)
            if u is not None: entry['unc_pct'] = u
        out.append(entry)
    # dedupe by mode (keep first)
    seen = {}; res = []
    for e in out:
        if e['mode'] not in seen: seen[e['mode']] = 1; res.append(e)
    return res

def read_datasets():
    """Yield (nucid, dsid_line, lines) for every dataset in every mass-chain file."""
    for path in sorted(glob.glob(os.path.join(RAW, 'ensdf.*'))):
        with open(path, encoding='latin-1') as f:
            block = []
            for line in f:
                line = line.rstrip('\n')
                if line.strip() == '':
                    if block: yield block; block = []
                else:
                    block.append(line.ljust(80))
            if block: yield block

def header(lines):
    h = lines[0]
    return {'nucid': h[0:5].strip(), 'dsid': h[9:39].strip(), 'dsref': h[39:65].strip(), 'pub': h[65:74].strip(), 'date': h[74:80].strip()}

def collect_levels(lines):
    """Parse L records with their continuations. Returns list of dicts in file order."""
    levels = []; cur = None; cont = ''
    for l in lines[1:]:
        nucid, c6, c8, c7 = l[0:5], l[5], l[6], l[7]   # c6 continuation, c8 comment flag, c7 record type
        if c7 == 'L' and c6 == ' ' and c8 == ' ':
            if cur: cur['cont'] = cont; levels.append(cur)
            cur = {'e': l[9:19].strip(), 'de': l[19:21].strip(), 'jp': l[21:39].strip(), 't': l[39:49], 'dt': l[49:55],
                   'ms': l[77:79].strip(), 'q': l[79]}
            cont = ''
        elif c7 == 'L' and c6 not in (' ',) and c8 == ' ' and cur is not None:
            cont += ' ' + l[9:80]
    if cur: cur['cont'] = cont; levels.append(cur)
    return levels

def evaluators(lines):
    """First 'H' (history) or the 'c' comment lines are not evaluator fields; ENSDF puts evaluators in the
    dataset's first comment records 'AUTH' in H records (newer) — capture AUTH= from H records if present."""
    txt = ' '.join(l[9:80] for l in lines if l[7] == 'H')
    m = re.search(r'AUT=([^$]+)', txt)
    return m.group(1).strip() if m else None

# ---------- pass 1: adopted levels ----------
nuclides = {}   # key -> entry
level_index = {}  # (z,a) -> list of (energy_keV, key) for isomers kept, for decay-dataset matching
adopted_headers = {}
for ds in read_datasets():
    h = header(ds)
    if not h['dsid'].startswith('ADOPTED LEVELS'): continue
    za = nucid_parse(h['nucid'])
    if not za: continue
    z, a = za
    lv = collect_levels(ds)
    if not lv: continue
    auth = evaluators(ds)
    kept = []
    for i, L in enumerate(lv):
        e = parse_value(L['e'].replace('+X','').replace('X','').replace('+Y','').replace('Y',''))
        hl = parse_halflife(L['t'], L['dt'])
        br = parse_branches(L['cont'])
        is_ground = (i == 0)
        non_it = [b for b in br if b['mode'] != 'IT']
        long_enough = hl and not hl.get('stable') and hl.get('seconds', 0) >= ISOMER_MIN_SEC
        if not (is_ground or long_enough):   # excited levels kept only with T1/2 >= ISOMER_MIN_SEC
            continue
        if not is_ground and not hl:   # an isomer flag without a half-life is useless to the network
            continue
        kept.append((i, L, e, hl, br))
    # label isomers m, n, p … in order of energy among kept excited levels
    iso_labels = ['m','n','p','q','r']
    ex = [k for k in kept if k[0] != 0]
    ex.sort(key=lambda k: (k[2] if k[2] is not None else 1e9))
    for idx, (i, L, e, hl, br) in enumerate(kept):
        if i == 0: iso = ''
        else:
            pos = [k[0] for k in ex].index(i)
            iso = iso_labels[pos] if pos < len(iso_labels) else f"x{pos}"
        key = key_of(z, a, iso)
        entry = {'z': z, 'a': a, 'element': ELEMENTS[z], 'isomer': iso, 'level_keV': e, 'jp': L['jp'],
                 'half_life': hl, 'branches': br,
                 'source': {'dsid': h['dsid'], 'nucid': h['nucid'], 'cutoff': h['pub'], 'edit': h['date'], 'dsref': h['dsref'], 'evaluators': auth}}
        if L['ms']: entry['ms_flag'] = L['ms']
        nuclides[key] = entry
        level_index.setdefault((z, a), []).append((e if e is not None else 0.0, key))
print(f"adopted: {len(nuclides)} states kept", file=sys.stderr)

# ---------- pass 2: decay datasets → isomer feeding ----------
DECAY_RE = re.compile(r'^(\d{1,3}[A-Z]{1,2})\s+(B-|B\+|EC|A|IT|SF|EC\+B\+)\s+DECAY(?:\s*\(([^)]*)\))?')
feeding = {}   # (parent_key, mode) -> {daughter_key: fraction_of_mode}
unresolved = set()
for ds in read_datasets():
    h = header(ds)
    m = DECAY_RE.match(h['dsid'])
    if not m: continue
    dz_a = nucid_parse(h['nucid']);  pz_a = nucid_parse(m.group(1))
    if not dz_a or not pz_a: continue
    mode = m.group(2); mode = 'EC+B+' if mode == 'EC+B+' else mode
    # which parent level? P record: cols 10-19 energy of parent level
    p_energy = 0.0
    for l in ds[1:]:
        if l[7] == 'P' and l[5] == ' ' and l[6] == ' ':
            p_energy = parse_value(l[9:19].replace('X','').replace('+','')) or 0.0; break
    # match parent key by nearest kept level energy
    cands = level_index.get(pz_a, [])
    if not cands: continue
    pe, pkey = min(cands, key=lambda c: abs(c[0] - p_energy))
    if abs(pe - p_energy) > 2.0 and p_energy > 0: continue  # dataset for an isomer we do not carry
    # daughter isomers to resolve
    dl = level_index.get(dz_a, [])
    iso_levels = [(e, k) for e, k in dl if e and e > 0]
    if not iso_levels: continue
    # normalization
    NR = NB = BR = None
    for l in ds[1:]:
        if l[7] == 'N' and l[5] == ' ' and l[6] == ' ':
            NR = parse_value(l[9:19]); BR = parse_value(l[31:39]); NB = parse_value(l[41:49])
    if NR is None: NR = 1.0
    if NB is None: NB = 1.0
    if BR is None: BR = 1.0
    # walk levels, accumulate direct feeding and gamma in/out per level
    levels = []  # [energy, direct, gamma_in, gamma_out]
    cur = None
    lvl_es = []
    for l in ds[1:]:
        c6, c8, c7 = l[5], l[6], l[7]
        if c7 == 'L' and c6 == ' ' and c8 == ' ':
            e = parse_value(l[9:19].replace('X','').replace('+',''))
            cur = {'e': e if e is not None else 0.0, 'direct': 0.0, 'gin': 0.0, 'gout': 0.0}
            levels.append(cur)
        elif cur is not None and c6 == ' ' and c8 == ' ' and c7 in ('B','E','A'):
            if c7 == 'B':
                ib = parse_value(l[21:29]); 
                if ib: cur['direct'] += ib * NB * BR
            elif c7 == 'E':
                ib = parse_value(l[21:29]); ie = parse_value(l[31:39]); ti = parse_value(l[64:74])
                if ti: cur['direct'] += ti * NB * BR
                else: cur['direct'] += ((ib or 0) + (ie or 0)) * NB * BR
            elif c7 == 'A':
                ia = parse_value(l[21:29])
                if ia: cur['direct'] += ia * BR   # alpha intensities per 100 decays via NB? ENSDF: IA per 100 alpha decays × BR
        elif cur is not None and c6 == ' ' and c8 == ' ' and c7 == 'G':
            eg = parse_value(l[9:19]); ri = parse_value(l[21:29]); ti = parse_value(l[64:74]); cc = parse_value(l[55:62])
            tot = ti if ti is not None else ((ri or 0.0) * (1.0 + (cc or 0.0)))
            tot *= NR * BR
            cur['gout'] += tot
            if eg is not None:
                # find destination level: energy ≈ E_level − Eγ (recoil ignored, tolerance 1.5 keV)
                target = cur['e'] - eg
                best = None
                for L2 in levels:
                    if abs(L2['e'] - target) <= 1.5 and L2 is not cur:
                        if best is None or abs(L2['e'] - target) < abs(best['e'] - target): best = L2
                if best is not None: best['gin'] += tot
    if not levels or all(L['direct'] == 0 and L['gin'] == 0 for L in levels):
        unresolved.add((pkey, mode)); continue
    total_pop = sum(L['direct'] for L in levels)
    if total_pop <= 0:
        unresolved.add((pkey, mode)); continue
    fr = {}
    for e, k in iso_levels:
        pop = 0.0
        for L in levels:
            if abs(L['e'] - e) <= 1.5:
                pop += L['direct'] + L['gin']   # the isomer's own de-excitation (listed as gammas out) is its decay, not a loss of population
        if pop > 0: fr[k] = pop / total_pop
    if fr:
        s = sum(fr.values())
        if s > 1.0: fr = {k: v / s for k, v in fr.items()}
        feeding[(pkey, mode)] = fr
print(f"decay datasets: {len(feeding)} parent/mode with isomer feeding resolved, {len(unresolved)} unresolved", file=sys.stderr)

# ---------- assemble network ----------
def daughter_key(z, a, mode):
    d = MODE_DZ_DA.get(mode)
    if d is None: return None
    dz, da = z + d[0], a + d[1]
    if dz < 0 or da < 1: return None
    return key_of(dz, da, '')

for key, n in nuclides.items():
    z, a = n['z'], n['a']
    trans = []
    if n['half_life'] and n['half_life'].get('stable'): n['transitions'] = []; continue
    # ENSDF convention: delayed-particle percentages (%B-N, %B+P, ...) are fractions of the parent
    # beta branch that are followed by particle emission — a subset, not an independent branch. If
    # only the delayed fraction is given, the parent beta branch is implied to be 100 %.
    PARENT_OF = {'B-N': 'B-', 'B-2N': 'B-', 'B-A': 'B-', 'B-P': 'B-', 'B+P': 'EC+B+', 'B+A': 'EC+B+', 'ECP': 'EC+B+', 'ECA': 'EC+B+'}
    pct = {b['mode']: b['pct'] for b in n['branches'] if 'pct' in b}
    def parent_key_for(pm):
        for cand in ((pm,) if pm != 'EC+B+' else ('EC+B+', 'EC', 'B+')):
            if cand in pct: return cand
        return None
    for dm, pm in PARENT_OF.items():
        if dm in pct:
            pk = parent_key_for(pm)
            if pk is None: pct[pm] = 100.0; pk = pm
            pct[pk] = max(pct[pk] - pct[dm], 0.0)
    if 'EC+B+' in pct:   # %EC and %B+ given alongside %EC+%B+ are its sub-shares, same daughter
        pct.pop('EC', None); pct.pop('B+', None)
    # Rounding excess: '%A=100 $ %SF=5.5E-7' — the minor branch sits inside the rounded major one.
    # If the modes sum to more than 100 by no more than 0.05 (a rounding-level amount), take the
    # excess out of the largest branch so that nuclei are conserved.
    tot = sum(pct.values())
    if 100.0 < tot <= 100.05 and pct:
        big = max(pct, key=pct.get); pct[big] -= (tot - 100.0)
    branch_list = [dict(b, pct=pct[b['mode']]) for b in n['branches'] if b['mode'] in pct]
    for m_ in pct:
        if m_ not in [b['mode'] for b in branch_list]: branch_list.append({'mode': m_, 'pct': pct[m_], 'implied': True})
    for b in branch_list:
        mode = b['mode']
        if 'pct' not in b: continue
        frac = b['pct'] / 100.0
        if mode == 'SF':
            trans.append({'mode': mode, 'fraction': frac, 'to': None}); continue
        base = daughter_key(z, a, mode)
        if base is None: continue
        if mode == 'IT':
            # IT goes to the next lower kept level of the same nuclide if any, else ground
            lower = sorted([(e, k) for e, k in level_index.get((z, a), []) if (n['level_keV'] or 0) > e], key=lambda t: -t[0])
            trans.append({'mode': mode, 'fraction': frac, 'to': lower[0][1] if lower else base}); continue
        fk = feeding.get((key, 'EC+B+' if mode in ('EC','B+','EC+B+') else mode)) or feeding.get((key, mode)) or {}
        rest = frac
        for dk, f in fk.items():
            if dk in nuclides:
                trans.append({'mode': mode, 'fraction': frac * f, 'to': dk}); rest -= frac * f
        if rest > 1e-12 or not fk:
            if base in nuclides: trans.append({'mode': mode, 'fraction': max(rest, 0.0), 'to': base})
            else: trans.append({'mode': mode, 'fraction': max(rest, 0.0), 'to': None, 'note': 'daughter not in table'})
        if (key, mode) in unresolved: n['isomer_feeding'] = 'unresolved'
    n['transitions'] = trans
    tot = sum(t['fraction'] for t in trans)
    if trans and abs(tot - 1.0) > 0.02: n['branch_sum'] = round(tot, 4)

meta = {'source': 'ENSDF', 'distribution': DIST, 'doi': '10.18139/nndc.ensdf/1845010',
        'built': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'), 'isomer_min_sec': ISOMER_MIN_SEC,
        'states': len(nuclides), 'builder': 'pipelines/build_nuclides.py'}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump({'meta': meta, 'nuclides': nuclides}, open(os.path.join(BUILD, 'nuclides_full.json'), 'w'), indent=0)
# shipped: drop raw branch text, keep what the runtime needs + provenance
ship = {}
for k, n in nuclides.items():
    hl = n['half_life']
    ship[k] = {'z': n['z'], 'a': n['a'], 'el': n['element'], 'iso': n['isomer'], 'E': n['level_keV'], 'jp': n['jp'],
               'stable': bool(hl and hl.get('stable')),
               't12': None if not hl or hl.get('stable') else hl['seconds'],
               't12_str': None if not hl or hl.get('stable') else f"{hl['value']:g} {hl['unit'].lower()}",
               't12_unc': None if not hl or hl.get('stable') else hl.get('unc_seconds'),
               'tr': [{'m': t['mode'], 'f': round(t['fraction'], 8), 'to': t['to']} for t in n['transitions']],
               'src': f"{n['source']['dsid']} ({n['source']['nucid']}), cut-off {n['source']['cutoff']}, edited {n['source']['edit']}"}
    if n.get('isomer_feeding'): ship[k]['flag'] = n['isomer_feeding']
    if n.get('branch_sum'): ship[k]['branch_sum'] = n['branch_sum']
json.dump({'meta': meta, 'nuclides': ship}, open(OUT, 'w'), separators=(',', ':'))
print(f"wrote {OUT}: {len(ship)} states, {os.path.getsize(OUT)/1e6:.2f} MB", file=sys.stderr)
