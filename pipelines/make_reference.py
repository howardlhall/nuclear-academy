#!/usr/bin/env python3
"""Independent high-precision reference for tests/decay.test.mjs: integrates dN/dt = A N with
mpmath at 50 digits using the exact triangular eigen-solution, for the same nuclide table the
site ships. Written deliberately without sharing code with src/lib/decay.js."""
import json, os, sys
from mpmath import mp, mpf, exp, log
mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
tab = json.load(open(os.path.join(HERE, '..', 'public', 'data', 'nuclides.json')))['nuclides']
LN2 = log(2)

def network(start):
    order, seen = [], set()
    def visit(k):
        if k in seen or k not in tab: return
        seen.add(k)
        for t in tab[k]['tr']:
            if t['to'] and t['to'] in tab: visit(t['to'])
        order.append(k)
    for k in start: visit(k)
    return order[::-1]

def solve(initial, times):
    order = network(list(initial))
    n = len(order); ix = {k: i for i, k in enumerate(order)}
    lam = [mpf(0) if tab[k]['stable'] or not tab[k]['t12'] else LN2 / mpf(repr(tab[k]['t12'])) for k in order]
    A = [[mpf(0)] * n for _ in range(n)]
    for j, k in enumerate(order):
        if lam[j] == 0: continue
        A[j][j] = -lam[j]
        for t in tab[k]['tr']:
            if t['to'] in ix and t['f'] > 0: A[ix[t['to']]][j] += lam[j] * mpf(repr(t['f']))
    # eigen-solution for radioactive nodes; stable by integral (independent derivation, same idea)
    rad = [i for i in range(n) if lam[i] != 0]
    m = len(rad); rp = {i: p for p, i in enumerate(rad)}
    C = [[mpf(0)] * m for _ in range(m)]
    for kk in range(m):
        C[kk][kk] = mpf(1)
        for ii in range(kk + 1, m):
            s = sum(A[rad[ii]][rad[jj]] * C[jj][kk] for jj in range(kk, ii))
            C[ii][kk] = s / (lam[rad[ii]] - lam[rad[kk]]) if s != 0 else mpf(0)
    N0 = [mpf(repr(initial.get(order[i], 0))) for i in rad]
    c = []
    for i in range(m):
        s = N0[i] - sum(C[i][k] * c[k] for k in range(i)); c.append(s)
    out = {k: [] for k in order}
    for t in times:
        t = mpf(repr(t))
        Nr = [sum(C[i][k] * c[k] * exp(-lam[rad[k]] * t) for k in range(i + 1)) for i in range(m)]
        Ir = [sum(C[i][k] * c[k] * ((1 - exp(-lam[rad[k]] * t)) / lam[rad[k]]) for k in range(i + 1)) for i in range(m)]
        vals = [mpf(0)] * n
        for p, i in enumerate(rad): vals[i] = Nr[p]
        for i in range(n):
            if lam[i] == 0:
                vals[i] = mpf(repr(initial.get(order[i], 0))) + sum(A[i][rad[p]] * Ir[p] for p in range(m))
        for i, k in enumerate(order): out[k].append(float(vals[i]))
    return out

cases = []
for name, initial, times in [
    ('U-238 series', {'U-238': 1e20}, [1.0, 1e6, 1e9, 1e12, 1e15, 1e17]),
    ('Th-232 series', {'Th-232': 1e20}, [1.0, 1e5, 1e8, 1e11, 1e14]),
    ('Mo-99 generator', {'Mo-99': 1e12}, [3600.0, 6 * 3600.0, 24 * 3600.0, 7 * 86400.0]),
    ('Cs-137', {'Cs-137': 1e15}, [60.0, 600.0, 86400.0, 30 * 365.25 * 86400.0]),
    ('mixed start', {'Ra-226': 1e14, 'Th-234': 1e10, 'Pb-210': 1e9}, [1e3, 1e6, 1e9]),
]:
    cases.append({'name': name, 'initial': initial, 'times': times, 'scale': max(initial.values()), 'N': solve(initial, times)})
json.dump({'generated_by': 'pipelines/make_reference.py (mpmath, 50 digits)', 'cases': cases},
          open(os.path.join(HERE, '..', 'tests', 'reference', 'bateman_reference.json'), 'w'), indent=0)
print('reference written:', [c['name'] for c in cases])
