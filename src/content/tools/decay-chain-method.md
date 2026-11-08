The network of nuclides reachable from the one you chose is assembled from the evaluated data,
with every decay mode and its branching fraction. Writing $N_i(t)$ for the number of atoms of
nuclide $i$, the inventories obey the coupled first-order equations

$$
\frac{dN_i}{dt} = -\lambda_i N_i + \sum_{j} \lambda_j\, b_{j\to i}\, N_j ,
$$

where $\lambda = \ln 2 / T_{1/2}$ and $b_{j\to i}$ is the fraction of decays of $j$ that produce
$i$. For a simple chain with a single starting nuclide this reduces to the Bateman equations
(1910):

$$
N_n(t) = N_1(0) \left(\prod_{i=1}^{n-1} \lambda_i\right) \sum_{i=1}^{n} \frac{e^{-\lambda_i t}}{\prod_{j \neq i} (\lambda_j - \lambda_i)} .
$$

The calculator solves the general branched system exactly, not by stepping in time: because
decay never runs backwards, the system's matrix is triangular, its eigenvalues are the
$-\lambda_i$, and the solution is $N(t) = C\, e^{-\Lambda t}\, C^{-1} N(0)$ with $C$ found by
a short recursion. Stable end products and the small fraction lost to spontaneous fission are
accumulated from the exact time-integral of the inflow, which avoids the zero-eigenvalue
degeneracy.

**Precision.** Double-precision arithmetic reproduces an independent 50-digit reference to
better than one part in $10^{8}$ across the U-238 and Th-232 series, and conserves the nucleus
count to one part in $10^{15}$. Two members of one lineage with decay constants equal to one
part in $10^{9}$ are separated by that amount and the fact is reported below the table. Values
smaller than the rounding error of their own summation are shown as zero.

**Data.** Half-lives and branching fractions come from the Evaluated Nuclear Structure Data File
(ENSDF, National Nuclear Data Center, Brookhaven National Laboratory; distribution of
1 September 2026, DOI [10.18139/nndc.ensdf/1845010](https://doi.org/10.18139/nndc.ensdf/1845010)),
read directly from the *Adopted Levels* datasets. Isomers with half-lives of one second or more
are carried as separate states; the split of a parent's β or ε decay between a daughter's ground
state and its isomer (Mo-99 → Tc-99m, 87.7 %) is obtained by balancing the intensities in the
corresponding decay dataset. Hovering a nuclide in the table shows the dataset, its evaluation
cut-off, and edit date. Delayed-particle branches (β⁻n and the like) are treated as ENSDF
records them, as sub-fractions of the parent β branch. Ninety-three states far from stability
carry incomplete branch sums in the evaluation; any unaccounted fraction is reported as
"removed from the network" rather than silently renormalized.

**Mass** uses the mass number as the molar mass, which is within 0.1 % for every nuclide.
