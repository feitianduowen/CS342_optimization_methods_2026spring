import numpy as np
import math

# ------------------------------------------------------------
# Exact formulas
# ------------------------------------------------------------

def dominance_probability_exact(m):
    return 0.5 ** m

def harmonic_number(n):
    return sum(1.0 / k for k in range(1, n + 1))

def expected_nd_exact_integral(n, m):
    """
    Exact expected number of non-dominated points.
    Uses mpmath numerical integration for m >= 2.

    Formula:
    E[M_{n,m}] = 1/(m-2)! * integral_0^inf
                 t^(m-2) * [1 - (1 - exp(-t))^n] dt
    """
    import mpmath as mp
    mp.mp.dps = 40

    if m == 2:
        return harmonic_number(n)

    f = lambda t: (t ** (m - 2)) * (1 - (1 - mp.e ** (-t)) ** n) / mp.factorial(m - 2)
    return float(mp.quad(f, [0, mp.inf]))


# ------------------------------------------------------------
# Monte Carlo simulation
# ------------------------------------------------------------

def dominance_probability_mc(m, trials=1_000_000, seed=0):
    rng = np.random.default_rng(seed)
    A = rng.random((trials, m))
    B = rng.random((trials, m))

    # Minimization convention: B dominates A if B_i <= A_i for all i.
    dominated = np.all(B <= A, axis=1)
    return dominated.mean()

def count_nondominated(points, minimize=True, block=256):
    """
    Count non-dominated points in a set.

    For minimization:
    point p is dominated by q if q_i <= p_i for all i
    and q_i < p_i for at least one i.

    The block implementation avoids creating one huge n x n x d array.
    """
    X = np.asarray(points)
    n, d = X.shape
    dominated = np.zeros(n, dtype=bool)

    for start in range(0, n, block):
        end = min(start + block, n)
        B = X[start:end]

        if minimize:
            weak = (X[:, None, :] <= B[None, :, :]).all(axis=2)
            strict = (X[:, None, :] < B[None, :, :]).any(axis=2)
        else:
            weak = (X[:, None, :] >= B[None, :, :]).all(axis=2)
            strict = (X[:, None, :] > B[None, :, :]).any(axis=2)

        dom = weak & strict
        dominated[start:end] = dom.any(axis=0)

    return np.sum(~dominated)

def expected_nd_mc(n, m, trials=1000, seed=0):
    rng = np.random.default_rng(seed)
    counts = []

    for _ in range(trials):
        points = rng.random((n, m))
        counts.append(count_nondominated(points, minimize=True))

    counts = np.array(counts)
    return counts.mean(), counts.std(ddof=1) / math.sqrt(trials)


# ------------------------------------------------------------
# Run all lab computations
# ------------------------------------------------------------

print("Dominance probabilities")
for m in [2, 4, 10]:
    exact = dominance_probability_exact(m)
    mc = dominance_probability_mc(m, trials=1_000_000, seed=123)
    print(f"m={m:2d}: exact={exact:.10f}, MC={mc:.10f}")

print("\nExpected number of non-dominated solutions")
cases = [
    (200, 2, 5000),
    (2000, 2, 1000),
    (200, 10, 500),
    (2000, 10, 50),   # Increase this if your computer is fast.
]

for n, m, trials in cases:
    exact = expected_nd_exact_integral(n, m)
    mc_mean, mc_se = expected_nd_mc(n, m, trials=trials, seed=123)
    print(
        f"n={n:4d}, m={m:2d}: "
        f"exact={exact:.6f}, MC={mc_mean:.6f}, SE={mc_se:.6f}, trials={trials}"
    )