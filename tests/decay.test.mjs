import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { solve, activities, LN2 } from '../src/lib/decay.js';

const table = JSON.parse(readFileSync(new URL('../public/data/nuclides.json', import.meta.url))).nuclides;
const rel = (a, b) => Math.abs(a - b) / Math.max(Math.abs(b), 1e-300);

test('single nuclide decays exponentially (Co-60)', () => {
  const t12 = table['Co-60'].t12;
  const times = [0, t12, 2 * t12, 10 * t12];
  const r = solve(table, { 'Co-60': 1e6 }, times);
  const i = r.order.indexOf('Co-60');
  assert.ok(rel(r.N[1][i], 5e5) < 1e-12);
  assert.ok(rel(r.N[2][i], 2.5e5) < 1e-12);
  assert.ok(rel(r.N[3][i], 1e6 / 1024) < 1e-11);
  const ni = r.order.indexOf('Ni-60');
  assert.ok(rel(r.N[3][ni], 1e6 * (1 - 1 / 1024)) < 1e-11, 'stable daughter accumulates');
});

test('two-member Bateman closed form (Sr-90 → Y-90 → Zr-90)', () => {
  const l1 = LN2 / table['Sr-90'].t12, l2 = LN2 / table['Y-90'].t12;
  const N0 = 1e9;
  for (const t of [3600, 86400, 30 * 86400, 5 * 365.25 * 86400]) {
    const r = solve(table, { 'Sr-90': N0 }, [t]);
    const ny = r.N[0][r.order.indexOf('Y-90')];
    const exact = N0 * l1 / (l2 - l1) * (Math.exp(-l1 * t) - Math.exp(-l2 * t));
    assert.ok(rel(ny, exact) < 1e-10, `t=${t}: ${ny} vs ${exact}`);
    const nz = r.N[0][r.order.indexOf('Zr-90')];
    const total = r.N[0].reduce((a, b) => a + b, 0);
    assert.ok(rel(total, N0) < 1e-10, 'heavy-nucleus count conserved');
  }
});

test('branching: Mo-99 → Tc-99m (87.7 %) and Tc-99 directly; Tc-99m → Tc-99', () => {
  const mo = table['Mo-99'];
  const bm = mo.tr.find((t) => t.to === 'Tc-99m').f;
  assert.ok(Math.abs(bm - 0.877) < 0.005, `Mo-99→Tc-99m fraction ${bm}`);
  const l1 = LN2 / mo.t12, l2 = LN2 / table['Tc-99m'].t12;
  const N0 = 1e12, t = 24 * 3600;
  const r = solve(table, { 'Mo-99': N0 }, [t]);
  const ntm = r.N[0][r.order.indexOf('Tc-99m')];
  const exact = bm * N0 * l1 / (l2 - l1) * (Math.exp(-l1 * t) - Math.exp(-l2 * t));
  assert.ok(rel(ntm, exact) < 1e-10);
});

test('secular equilibrium: Ra-226 progeny activities approach the parent after 1 year', () => {
  const r = solve(table, { 'Ra-226': 1e15 }, [365.25 * 86400]);
  const A = activities(r)[0];
  const ap = A[r.order.indexOf('Ra-226')];
  for (const k of ['Rn-222', 'Po-218', 'Pb-214', 'Bi-214', 'Po-214']) {
    const a = A[r.order.indexOf(k)];
    assert.ok(rel(a, ap) < 2e-3, `${k}: ${a} vs ${ap}`);
  }
  // Pb-210 (22 y) is far from equilibrium after 1 y: ratio ≈ 1 − e^{−λt}
  const lpb = LN2 / table['Pb-210'].t12;
  const apb = A[r.order.indexOf('Pb-210')];
  assert.ok(rel(apb / ap, 1 - Math.exp(-lpb * 365.25 * 86400)) < 2e-2); // ingrowth lags by the Rn-222 (3.8 d) step
});

test('conservation across the whole U-238 series incl. sinks', () => {
  const N0 = 1e20;
  const times = [1, 1e6, 1e9, 1e12, 1e15, 1e17, 1e19];
  const r = solve(table, { 'U-238': N0 }, times);
  for (let ti = 0; ti < times.length; ti++) {
    let total = r.N[ti].reduce((a, b) => a + b, 0);
    for (const s of Object.values(r.sinks)) total += s[ti];
    assert.ok(rel(total, N0) < 1e-7, `t=${times[ti]}: total ${total}`); // end-product accumulation carries ~1e-8 relative error on this 20-decade chain
    for (const v of r.N[ti]) assert.ok(v >= 0, 'no negative inventories');
  }
  const pb = r.N[6][r.order.indexOf('Pb-206')];
  assert.ok(pb / N0 > 0.9999, 'nearly all Pb-206 after 1e19 s (~70 half-lives)');
});

test('reference: high-precision mpmath solution of the Th-232 and U-238 series', () => {
  const ref = JSON.parse(readFileSync(new URL('./reference/bateman_reference.json', import.meta.url)));
  for (const c of ref.cases) {
    const r = solve(table, c.initial, c.times);
    for (const [k, vals] of Object.entries(c.N)) {
      const i = r.order.indexOf(k);
      vals.forEach((v, ti) => {
        const ours = r.N[ti][i];
        const tol = Math.abs(v) > 1e-3 * c.scale ? 1e-8 : 1e-6 * c.scale; // relative for material amounts, absolute for traces
        const ok = Math.abs(v) > 1e-3 * c.scale ? rel(ours, v) < tol : Math.abs(ours - v) < tol;
        assert.ok(ok, `${c.name} ${k} t=${c.times[ti]}: ${ours} vs ref ${v}`);
      });
    }
  }
});
