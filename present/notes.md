## Measurements
We measure by projecting our state onto some known state.  We can do this by use one of the following tools for measurements:
- QWP: Quarter Wave Plate
- HWP: Half Wave Plate
- PBS: Polarising Beam Splitter
- Polarizer

1. Method 1: QWP + Polariser
QWP can be used to rotate any state onto a linear polarization state.  We can then use a polarizer to project onto the desired linear polarisation state.

2. Method 2: QWP + HWP + PBS
QWP + HWP are used to rotate our state into horizontal. The beam spiters then transmits the horizontal component and reflects the vertical component.

When we wish to change the basis we can just rotate the QWP, HWP and Polarisers to the desired basis.

### State Tomography
Rather than measure our state, here we see the overlap of our state with a set of known states (these known states should form a basis). We can then reconstruct our state from the statistics.

To find a state on the poincare sphere we project it onto 3axes
- L/R (Left/Right, Circular)
- H/V (Horizontal/Vertical, Linear)
- D/A (Diagonal/Anti-Diagonal, Linear)

<!-- ![Poincare Sphere](https://upload.wikimedia.org/wikipedia/commons/d/dc/Poincare-sphere_stokes.svg) -->

**IDEALLY:** We technically need 4 measurements, 1 for each axis + 1 for normalization. So say, H+D+L for the axes, then also R since L+R=1 so we can normalize.

**REALITY:**
- Problem: Power may fluctuate, \
Solution: Use PBS to measure both states for a basis at once
- Problem: Transmission may not be same for all bases, \
Solution: Make 6 measurements, H+V+D+A+L+R
- Problem: Projections can give 'unphysical' states. So say if there is any point ON a poincare sphere, its possible errors bring it OUTSIDE the sphere. \
Solution: Use a Maximum Likelihood Estimator (MLE) to find the closest point on the sphere (or Bayesian Tomography)

#### MLE
Create a likelyhood function
$$
LF = f(N_1, ..., N_n;\theta_1, ..., \theta_n)
$$
Which gives the probability of outcomes $N_i$ for a parameter $\theta_j$.

For fully independent measurements, the likelyhood function is the product of the individual likelyhoods
$$
LF = \prod_{i=1} p(N_i;\theta_1, ..., \theta_m)
$$

A good MLE tells are which parameters are most likely to contain the data we need.

Example: Consider a coin flip: where with $P(H) = \theta$, we flip coin $N$ times with $N_h$ heads and $N-N_h$ tails. The likelyhood function is
$$
f(N_h, N-N_h; \theta) = \theta^{N_h}(1-\theta)^{N-N_h}
$$
So the log likelyhood function is
$$
\log f(N_h, N-N_h; \theta) = N_h \log \theta + (N-N_h) \log (1-\theta)
$$
which is maximised when $\theta = \frac{N_h}{N}$ which is the maximum likelyhood estimator.

- So if we wanted to know which state $\rho$ most likely generate out measurements $N_H, N_V, N_D, N_A, N_L, N_R$ we would need to find the maximum of the likelyhood function
- We avg each measurement as \
$\bar{N_x} = (N_x + N_{x\perp})\langle x| \rho_{\text{test}} |x \rangle$ where $\rho_{\text{test}}$ is the test state we use to maximise over
- $p(N_x;\rho_{\text{test}}) = e^{-\frac{(N_x-\bar{N_x})^2}{2N_x}}$. The distribution of light is generally Poissonian, but for large numbers we can approximate it with a Gaussian distribution.
- Maximise $f(N_H, ..., N_R; \rho_{\text{test}}) = e^{-\frac{(N_H-\bar{N_H})^2}{2N_H}} \times ... \times e^{-\frac{(N_R-\bar{N_R})^2}{2N_R}}$ to find true state $\rho$.

### Process Tomography
General process is $|\psi\rangle \rightarrow U|\psi\rangle$ where $U$ is some unitary operator or $|\rho\rangle \rightarrow \rho' = U\rho U^\dagger$ where $U$ is some unitary operator.

In general we can generalise quantum processes as
$$
\rho \rightarrow \epsilon(\rho) = \sum_i E_i \rho E_i^\dagger \\
\text{where } \sum_i E_i^\dagger E_i = I
$$
where $E_i$ are the Kraus operators. Examples:
1. HWP at 0&deg;: $\epsilon(\rho) = Z\rho Z$
2. Dephasing: $\epsilon(\rho) = \frac{1}{2}(I\rho I + Z\rho Z)$, this basically takes all off diagonal elements and makes them 0. i.e \
$\begin{pmatrix} a & b \\ b* & 1-a \end{pmatrix} \rightarrow \begin{pmatrix} a & 0 \\ 0 & 1-a \end{pmatrix}$

So when we measure this what are we actually measuring
- $\epsilon(\rho) = \sum_i E_i \rho E_i^\dagger$
- We can always write $E_i$ in terms of paulis\
$E_i = \sum_j c_{ij} \sigma_j$ where $\sigma_j$ are the pauli matrices
- So $\epsilon(\rho) = \sum_{i,j,k} c_{ij} c_{ik} \sigma_j \rho \sigma_k$ = $\sum_{j,k} \chi_{jk} \sigma_j \rho \sigma_k$
- such that $\chi_{jk} = \sum_{i} c_{ij} c_{ik}$

So we can note that the $\chi$ matrix which is hermitian can fully determine our state $\epsilon(\rho)$.

## Gentle Measurement
The problem with measurement is that everytime we measure a state, there is a large change in some variable. Ex if a value is 0.5 we force it to be 0 or 1. This is a large change. We can instead use a gentle measurement which only slightly changes the state.

This is done by dependence of knowing some info about the state before hand and measuring it in a situaiton closest to its eigenvalues. This will allow us to change the state by a small amount.

### Differential Privacy
We compare this to Differeintial Privacy where we can only change the state by a small amount. S.t
$$
log \frac{P(M|s)}{P(M|s')} \leq \epsilon
$$
Where $s$ is the original state, $s'$ is the new state and $M$ is the measurement on a database. Here $s$ and $s'$ are very similar and often differ by one record. The objective is to make sure that the change is arbitrarily small. This $\epsilon$ is the privacy budget.

We often rewrite this as
$$
P(M|s) \leq e^\epsilon P(M|s') + \delta
$$
Where $\delta$ is the probability of failure. This is the probability that the measurement fails. And we do this multiplicative form because it is easy to compose multiple measurements. Note: $e^\epsilon \approx 1 + \epsilon$ for small $\epsilon$.

The composition can be seen as such: If we have two algorithms with a privacy budget of $\epsilon_1$ and $\epsilon_2$ and failure rates of $\delta_1$ and $\delta_2$ then the composition of the two algorithms gives us a new NET required privacy budget of
$$
\epsilon = (\epsilon_1 + \epsilon_2) - (\delta_1 + \delta_2)
$$

### Applying Differential Privacy to ML
We can apply this to ML by adding noise to the data. This
- Makes it harder to reverse engineer the data
- Makes it harder to overfit the data
- Makes it harder to memorise the data

So consider Stochastic Gradient Descent (SGD) which we can modify to DP-SGD as follows:
For each epoch when calculating gradient $\nabla \mathcal{L}$ we first clip the gradient to some norm $C$ as follows
$$
\bar{g} = \frac{g}{max(1, \frac{||g||_2}{C})}
$$
This very intuitively limits the amount of information we learn from a given example. We then add noise to the gradient as follows
$$
\bar{g} = \bar{g} + \mathcal{N}(0, \sigma^2 C^2 I)
$$
Where $\sigma$ is the noise multiplier and both $\sigma$ and $C$ are hyperparameters that can be tuned to ensure the desired privacy budget.

### Calculating Privacy Budget
The above was for ONE STEP of the SGD, for a total budget, we first calculate the budget for each step as: $q\epsilon - q\delta$ where $q$ is the probability of sampling a given example. Then we sum over all steps to get the total budget. So the total budget is $T(q\epsilon - q\delta)$ where $T$ is the number of steps. From strong composition theorem we can get however an even tighter bound of
$$
\epsilon_{\text{Total}} = O(q\epsilon\sqrt{T\log(1/\delta)} - Tq\delta)
$$
There also exists an optimisation where we realise that Privacy Loss Distribution is a long tailled distribution and so we can use the moments accountant bound the failure rate to $\delta$ rather than $Tq\delta$.

### Applying Differential Privacy to Gentle Measurement
Now when we return the result of a measurement, rather than returning the actual result, we return a noisy version of the result. This is done by adding noise Laplace noise ($e^{-\epsilon|k|}$)

We define a Quantum Measurement as &alpha;-Gentle if
$$
||\rho_{M\rightarrow y} - \rho||_{tr} \leq \alpha
$$
For a measurement $M$ on a set of states $\rho \in \mathcal{S}$ and every possible outcome $y$.

Consider an $n$ qubit state $(\alpha|0\rangle + \beta|1\rangle)^{\otimes n}$ and we have to count the number of 1s (Hamming Weight) of the resultant string.

We know generally the the state is currently $(\alpha|0\rangle + \beta|1\rangle)^{\otimes n} \rightarrow \sum_{x\in\{0,1\}^n : |x|=k} |x\rangle$ (ignoring normalisation). We can see how every measurement destroys the state by a lot.

So we insert deliberately added noise as $Pr[\eta] = \frac{1}{2\sigma}e^{-\frac{|\eta|}{\sigma}}$ so we get in return

$$
\sum_{x\in\{0,1\}^n} \alpha_x|x\rangle\sum_n \sqrt{Pr[\eta]}||x|+n\rangle
$$
Which is the hamming weight of $x$ plus noise $\eta$. This can be done with fully quantum processes by preparing a superposition of all possible values of the laplace noise and add the unitary $U_\eta$ which adds the noise to the state.

There also exists proof in both directions btw which show that Gentle Measurements are DP and DP measurements are Gentle.

## Shadow Tomography
The complexity of traditional tomography is $O(d^2)$ where $d$ is the dimension of the state. We understand that this $d$ is exponential

### Postselected Learning Theory
If A wants to send B a D-dim mixed state $\rho$ such that B can estimate $Tr(E_i\rho)$ to within $\pm\epsilon$ for any of M two-outcome measurements $E_i$, then A needs to send AT MOST

$$
\tilde{O}(\frac{n\log M}{e^3}) \text{ Classical Bits}
$$

- applying this to shadow tomography we can now get $Tr(E_i\rho)$ to within $\pm\epsilon$ for any of M two-outcome measurements $E_i$ FOR ALL $i$ within $k$ copies of $\rho$ where
  $$
  k = \tilde{O}(\frac{n\log^4 M}{e^5})
  $$
- or when we don't want $\rho$ but some M linear features as $tr(O_1\rho)...tr(O_M\rho)$ $k$ copies of $\rho$ where
  $$
  k = \tilde{O}(\frac{n^2\log^2 M}{e^8})
  $$

## Classical Shadow Theorem
There is a procedure that guarantees the following.
1. Given B, $\epsilon$ > 0, the procedure learns a classical representation of p from $N$ measurements where $N$ is:
$$
N = \tilde{O}(\frac{B\log M}{\epsilon^2})
$$
2. Subsequently, given any $O_1, ..., O_M$ with $B \geq max ||O_i||^2_{\text{shadow}}$ the procedure can use the classical representation to predict $o_1, ..., o_M$ where $|o_i - tr(O_i\rho)| < \epsilon$ for all $i$.

> Here: $max ||O_i||^2_{\text{shadow}}$ is a shadow norm which we require to be small. This thankfully is independent of system size.

## Gist
In classical tomography we sample in a fixed pattern and correct for noise. In shadow tomography we sample in a random pattern the noise sort of cancels out. Generally we sample $U_i \in \mathbb{Cl}(2^n)$ i.e we sample unitaries from the Clifford Group and apply to them to our state $\rho$ as $U_i\rho U_i^\dagger$ and then measure in the computational basis.  