/**
 * decay.js — radioactive decay network solver (Bateman equations with branching).
 *
 * Model: dN/dt = A·N with A_ii = −λ_i and A_ij = λ_j·b(j→i) for every transition j→i with
 * branching fraction b. Because decay never cycles, the network can be ordered so that A is
 * lower-triangular; its eigenvalues are the −λ_i, and the exact solution is
 *     N(t) = C · diag(exp(−λ t)) · C⁻¹ · N(0)
 * with C the (unit lower-triangular) eigenvector matrix, computed by forward recursion
 *     C_ik = Σ_{j<i} A_ij C_jk / (λ_i − λ_k)          (i > k),  C_kk = 1.
 * Stable nuclides (λ = 0) and other sinks (spontaneous fission, unknown remainder, nuclides
 * missing from the table) are handled outside the eigen-solution: their inventory is the
 * initial value plus the time-integral of inflow, ∫e^{−λs}ds = (1 − e^{−λt})/λ, which avoids
 * the zero-eigenvalue degeneracy entirely.
 *
 * Numerical notes: the recursion suffers catastrophic cancellation when two radioactive members
 * of the same lineage have nearly equal decay constants. Pairs closer than DEGENERACY_REL are
 * separated by a symmetric relative nudge of that size and the fact is reported in
 * result.notes — the induced error is of the same order as the nudge, far below the data's
 * uncertainties. Chains with very disparate half-lives (U-238 series, 1e-18 to 1e2 s⁻¹) are
 * well-conditioned for this method; validation cases are in tests/.
 *
 * Copyright Howard L. Hall; CC BY-NC-ND 4.0.
 */
export const LN2 = Math.LN2;
export const DEGENERACY_REL = 1e-9;

/** Collect the sub-network reachable from the given keys. Returns ordered node list (parents first). */
export function buildNetwork(table, startKeys) {
  const order = [];
  const seen = new Set();
  const sinks = new Map(); // synthetic sink keys → label
  function visit(key) {
    if (seen.has(key)) return;
    seen.add(key);
    const n = table[key];
    if (!n) return;
    for (const t of n.tr || []) {
      if (t.to && table[t.to]) visit(t.to);
    }
    order.push(key); // post-order: descendants first
  }
  for (const k of startKeys) visit(k);
  order.reverse(); // parents first
  // topological check: in a decay network reversed post-order is a valid topological order
  return order;
}

/**
 * Solve the network.
 * @param table   nuclide table (from src/data/nuclides.json .nuclides)
 * @param initial {key: atoms} initial inventories
 * @param times   array of times in seconds
 * @returns {order, lambda, N: Float64Array[times][nodes], sinks: {name: Float64Array[times]}, notes: []}
 */
export function solve(table, initial, times) {
  const startKeys = Object.keys(initial).filter((k) => initial[k] > 0);
  const order = buildNetwork(table, startKeys);
  const idx = new Map(order.map((k, i) => [k, i]));
  const n = order.length;
  const notes = [];

  // decay constants; stable → 0
  const lam = new Float64Array(n);
  for (let i = 0; i < n; i++) {
    const e = table[order[i]];
    lam[i] = e.stable || !e.t12 ? 0 : LN2 / e.t12;
  }
  const radio = []; // indices of radioactive nodes in topological order
  for (let i = 0; i < n; i++) if (lam[i] > 0) radio.push(i);
  const rpos = new Map(radio.map((i, p) => [i, p]));
  const m = radio.length;

  // degeneracy nudge among radioactive nodes that share a lineage (cheap: check all pairs)
  const lr = new Float64Array(m);
  for (let p = 0; p < m; p++) lr[p] = lam[radio[p]];
  for (let p = 0; p < m; p++) for (let q = p + 1; q < m; q++) {
    const a = lr[p], b = lr[q], mx = Math.max(a, b);
    if (Math.abs(a - b) < DEGENERACY_REL * mx) {
      const d = DEGENERACY_REL * mx;
      lr[p] = a + d; lr[q] = b - d;
      notes.push(`Decay constants of ${order[radio[p]]} and ${order[radio[q]]} differ by less than ${DEGENERACY_REL} relative; separated numerically by that amount.`);
    }
  }

  // transition rates into radioactive/sink nodes: from j (radio) to i: rate coefficient A_ij = λ_j b
  // build adjacency: for each radioactive node j, list of {to: index or sink name, b}
  const out = radio.map(() => []);
  const sinkNames = new Set(['spontaneous fission', 'unaccounted']);
  for (let p = 0; p < m; p++) {
    const j = radio[p];
    const e = table[order[j]];
    let acc = 0;
    for (const t of e.tr || []) {
      if (!(t.f > 0)) continue;
      acc += t.f;
      if (t.m === 'SF' || !t.to) { out[p].push({ sink: t.m === 'SF' ? 'spontaneous fission' : 'unaccounted', b: t.f }); continue; }
      if (!table[t.to]) { out[p].push({ sink: 'unaccounted', b: t.f }); sinkNames.add('unaccounted'); continue; }
      out[p].push({ to: idx.get(t.to), b: t.f });
    }
    if (acc < 1 - 1e-6) out[p].push({ sink: 'unaccounted', b: 1 - acc });
    else if (acc > 1 + 1e-6) notes.push(`${order[j]}: listed branches sum to ${(acc * 100).toFixed(2)} %; used as given.`);
  }

  // eigenvector matrix C (m×m, unit lower triangular in radio order) — C[i][k]
  const C = Array.from({ length: m }, () => new Float64Array(m));
  for (let k = 0; k < m; k++) {
    C[k][k] = 1;
    for (let i = k + 1; i < m; i++) {
      // Σ_j A_ij C_jk over radioactive j feeding i, j<i
      let s = 0;
      for (let j = k; j < i; j++) {
        if (C[j][k] === 0) continue;
        for (const tr of out[j]) if (tr.to !== undefined && rpos.get(tr.to) === i) s += lr[j] * tr.b * C[j][k];
      }
      C[i][k] = s === 0 ? 0 : s / (lr[i] - lr[k]);
    }
  }
  // c = C⁻¹ N0 by forward substitution (C unit lower triangular)
  const N0 = new Float64Array(m);
  for (let p = 0; p < m; p++) N0[p] = initial[order[radio[p]]] || 0;
  const c = new Float64Array(m);
  for (let i = 0; i < m; i++) {
    let s = N0[i];
    for (let k = 0; k < i; k++) s -= C[i][k] * c[k];
    c[i] = s;
  }

  // evaluate
  const T = times.length;
  const N = Array.from({ length: T }, () => new Float64Array(n));
  const sinks = {};
  for (const s of sinkNames) sinks[s] = new Float64Array(T);
  const stableInit = new Float64Array(n);
  for (let i = 0; i < n; i++) if (lam[i] === 0) stableInit[i] = initial[order[i]] || 0;
  const EPS = 64 * Number.EPSILON; // a result smaller than this × the sum of |terms| is rounding noise → 0

  for (let ti = 0; ti < T; ti++) {
    const t = times[ti];
    const ex = new Float64Array(m), integ = new Float64Array(m);
    for (let k = 0; k < m; k++) {
      const x = lr[k] * t;
      ex[k] = Math.exp(-x);
      integ[k] = x < 1e-8 ? t * (1 - x / 2) : (1 - ex[k]) / lr[k]; // ∫₀ᵗ e^{-λs} ds
    }
    // radioactive inventories and their time-integrals
    const Ni = new Float64Array(m), Ii = new Float64Array(m);
    for (let i = 0; i < m; i++) {
      let s = 0, q = 0, sAbs = 0, qAbs = 0;
      for (let k = 0; k <= i; k++) {
        const w = C[i][k] * c[k]; if (w === 0) continue;
        const a = w * ex[k], b = w * integ[k];
        s += a; q += b; sAbs += Math.abs(a); qAbs += Math.abs(b);
      }
      Ni[i] = Math.abs(s) <= EPS * sAbs ? 0 : s;
      Ii[i] = Math.abs(q) <= EPS * qAbs ? 0 : q;
      N[ti][radio[i]] = Ni[i];
    }
    // stable nuclides and sinks: initial + Σ_j λ_j b ∫N_j
    for (let i = 0; i < n; i++) if (lam[i] === 0) N[ti][i] = stableInit[i];
    for (let p = 0; p < m; p++) {
      const flow = lr[p] * Ii[p];
      for (const tr of out[p]) {
        if (tr.sink) sinks[tr.sink][ti] += tr.b * flow;
        else if (lam[tr.to] === 0) N[ti][tr.to] += tr.b * flow;
      }
    }
    for (let i = 0; i < n; i++) if (N[ti][i] < 0) N[ti][i] = 0; // stable accumulations: residual rounding only
    for (const s of Object.values(sinks)) if (s[ti] < 0) s[ti] = 0;
  }
  return { order, lambda: Array.from(lam), N, sinks, notes };
}

/** Activity in Bq for each node at each time. */
export function activities(res) {
  return res.N.map((row) => row.map((v, i) => v * res.lambda[i]));
}

/** Convenience: atoms from activity. */
export function atomsFromActivity(bq, t12s) { return (bq * t12s) / LN2; }

/** Approximate mass in grams from atom count (mass number as molar mass; ±0.1 %). */
export const AVOGADRO = 6.02214076e23;
export function gramsFromAtoms(atoms, massNumber) { return (atoms * massNumber) / AVOGADRO; }

export const TIME_UNITS = { s: 1, min: 60, h: 3600, d: 86400, y: 365.25 * 86400 };
export function formatHalfLife(sec) {
  if (sec == null) return 'stable';
  const u = [['y', 365.25 * 86400], ['d', 86400], ['h', 3600], ['min', 60], ['s', 1], ['ms', 1e-3], ['µs', 1e-6], ['ns', 1e-9]];
  for (const [name, f] of u) if (sec >= f * 0.999) return `${(sec / f).toPrecision(4).replace(/\.?0+$/, '')} ${name}`;
  return `${sec.toExponential(2)} s`;
}
