---
layout: ../../layouts/Page.astro
title: "Decay-chain calculator"
description: "Bateman-equation solutions for radioactive decay chains."
---

*In preparation.* Solves the Bateman equations for a chain of nuclides and plots activity and atom
number against time.

For a chain $N_1 \to N_2 \to \cdots \to N_n$ with decay constants $\lambda_i$ and only
$N_1(0) \neq 0$:

$$
N_n(t) = N_1(0) \left(\prod_{i=1}^{n-1} \lambda_i\right) \sum_{i=1}^{n} \frac{e^{-\lambda_i t}}{\prod_{j \neq i} (\lambda_j - \lambda_i)}
$$
