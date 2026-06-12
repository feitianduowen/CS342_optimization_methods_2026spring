import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# =========================
# 1. Objective functions
# =========================

def f1(x):
    """
    f1(x) = (x1 + 1)^2 / 9 + (x2 + 1)^2
    """
    return ((x[0] + 1.0) ** 2) / 9.0 + (x[1] + 1.0) ** 2


def grad_f1(x):
    """
    gradient of f1
    """
    return np.array([
        2.0 * (x[0] + 1.0) / 9.0,
        2.0 * (x[1] + 1.0)
    ])


def f2(x):
    """
    Rosenbrock function:
    f2(x) = (1 - x1)^2 + 100(x2 - x1^2)^2
    """
    x1, x2 = x
    return (1.0 - x1) ** 2 + 100.0 * (x2 - x1 ** 2) ** 2


def grad_f2(x):
    """
    gradient of Rosenbrock function
    """
    x1, x2 = x
    return np.array([
        2.0 * (x1 - 1.0) - 400.0 * x1 * (x2 - x1 ** 2),
        200.0 * (x2 - x1 ** 2)
    ])


def f3(x):
    """
    Own test function:
    f3(x) = 0.5*x1^2 + 25*x2^2
    """
    return 0.5 * x[0] ** 2 + 25.0 * x[1] ** 2


def grad_f3(x):
    """
    gradient of f3
    """
    return np.array([
        x[0],
        50.0 * x[1]
    ])


# =========================
# 2. Gradient descent with momentum
# =========================

def gradient_descent_with_momentum(f, grad, x0, alpha, beta, max_iter=1000):
    """
    Standard GD:
        x(k+1) = x(k) - alpha * grad f(x(k))

    GD with momentum:
        x(k+1) = x(k) - alpha * grad f(x(k)) + beta * (x(k) - x(k-1))

    Parameters:
        f        : objective function
        grad     : gradient function
        x0       : initial solution
        alpha    : constant step size
        beta     : momentum coefficient
        max_iter : maximum number of iterations

    Returns:
        xs   : sequence of solutions
        vals : sequence of objective function values
    """
    x_prev = np.array(x0, dtype=float)
    x = np.array(x0, dtype=float)

    xs = [x.copy()]
    vals = [f(x)]

    for k in range(max_iter):
        x_next = x - alpha * grad(x) + beta * (x - x_prev)

        xs.append(x_next.copy())
        vals.append(f(x_next))

        if not np.all(np.isfinite(x_next)):
            break

        x_prev = x
        x = x_next

    return np.array(xs), np.array(vals)


# =========================
# 3. Plotting function
# =========================

def plot_trajectory(f, experiments, x_range, y_range, title, optimum=None, log_contour=False):
    """
    Plot contour lines and optimization trajectories.
    """
    x1 = np.linspace(x_range[0], x_range[1], 400)
    x2 = np.linspace(y_range[0], y_range[1], 400)
    X1, X2 = np.meshgrid(x1, x2)

    Z = np.zeros_like(X1)
    for i in range(X1.shape[0]):
        for j in range(X1.shape[1]):
            Z[i, j] = f(np.array([X1[i, j], X2[i, j]]))

    plt.figure(figsize=(7, 6))

    if log_contour:
        levels = np.logspace(-2, 4, 25)
        plt.contour(X1, X2, Z, levels=levels, norm=mcolors.LogNorm())
    else:
        plt.contour(X1, X2, Z, levels=25)

    for label, xs, vals in experiments:
        plt.plot(
            xs[:, 0],
            xs[:, 1],
            marker="o",
            markersize=2,
            linewidth=1.2,
            label=label
        )

    if optimum is not None:
        plt.scatter(
            [optimum[0]],
            [optimum[1]],
            marker="*",
            s=150,
            label="Optimum"
        )

    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_convergence(experiments, title):
    """
    Plot objective value convergence curve.
    """
    plt.figure(figsize=(7, 5))

    for label, xs, vals in experiments:
        vals_plot = np.maximum(vals, 1e-16)
        plt.plot(np.arange(len(vals_plot)), vals_plot, label=label)

    plt.yscale("log")
    plt.xlabel("Iteration $k$")
    plt.ylabel("$f(x^{(k)})$")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()


# =========================
# 4. Experiments
# =========================

summary_rows = []

def clip_path_for_plot(xs, vals, xlim=(-2, 2), ylim=(-1, 3), fmax=1e6):
    """
    Hide points that go outside the plotting window or become too large.
    This prevents divergent trajectories from ruining the scale.
    """
    xs_plot = xs.copy()

    mask = (
        np.isfinite(xs_plot[:, 0]) &
        np.isfinite(xs_plot[:, 1]) &
        np.isfinite(vals) &
        (xs_plot[:, 0] >= xlim[0]) &
        (xs_plot[:, 0] <= xlim[1]) &
        (xs_plot[:, 1] >= ylim[0]) &
        (xs_plot[:, 1] <= ylim[1]) &
        (vals <= fmax)
    )

    xs_plot[~mask] = np.nan
    return xs_plot


def run_experiment(function_name, f, grad, x0, alpha, betas, max_iter, optimum):
    experiments = []

    for beta in betas:
        xs, vals = gradient_descent_with_momentum(
            f=f,
            grad=grad,
            x0=x0,
            alpha=alpha,
            beta=beta,
            max_iter=max_iter
        )

        label = f"alpha={alpha}, beta={beta}"
        experiments.append((label, xs, vals))

        hit = np.where(vals < 1e-6)[0]

        summary_rows.append({
            "function": function_name,
            "alpha": alpha,
            "beta": beta,
            "iterations": len(vals) - 1,
            "final_x1": xs[-1, 0],
            "final_x2": xs[-1, 1],
            "final_f": vals[-1],
            "best_f": np.min(vals),
            "first_iter_f_less_than_1e-6": int(hit[0]) if len(hit) > 0 else None
        })

    return experiments

def plot_rosenbrock_trajectory(experiments):
    x_range = (-2, 2)
    y_range = (-1, 3)

    x1 = np.linspace(x_range[0], x_range[1], 500)
    x2 = np.linspace(y_range[0], y_range[1], 500)
    X1, X2 = np.meshgrid(x1, x2)

    Z = np.zeros_like(X1)
    for i in range(X1.shape[0]):
        for j in range(X1.shape[1]):
            Z[i, j] = f2(np.array([X1[i, j], X2[i, j]]))

    plt.figure(figsize=(7, 6))

    levels = np.logspace(-2, 4, 25)
    plt.contour(X1, X2, Z, levels=levels, norm=mcolors.LogNorm())

    for label, xs, vals in experiments:
        xs_plot = clip_path_for_plot(
            xs,
            vals,
            xlim=x_range,
            ylim=y_range,
            fmax=1e6
        )

        plt.plot(
            xs_plot[:, 0],
            xs_plot[:, 1],
            marker="o",
            markersize=2,
            linewidth=1.2,
            label=label
        )

    plt.scatter([1.0], [1.0], marker="*", s=150, label="Optimum")

    plt.xlim(x_range)
    plt.ylim(y_range)

    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.title("Function 2: Rosenbrock Function")
    plt.legend()
    plt.tight_layout()
    plt.show()

# -------------------------
# Function 1
# -------------------------

experiments_f1 = run_experiment(
    function_name="f1",
    f=f1,
    grad=grad_f1,
    x0=np.array([4.0, -4.0]),
    alpha=0.30,
    betas=[0.0, 0.5, 0.98],
    max_iter=150,
    optimum=np.array([-1.0, -1.0])
)

plot_trajectory(
    f=f1,
    experiments=experiments_f1,
    x_range=(-5, 5),
    y_range=(-5, 5),
    title="Function 1: Gradient Descent with Momentum",
    optimum=np.array([-1.0, -1.0]),
    log_contour=False
)

plot_convergence(
    experiments=experiments_f1,
    title="Function 1: Convergence"
)


# -------------------------
# Function 2: Rosenbrock
# -------------------------

experiments_f2 = run_experiment(
    function_name="f2_Rosenbrock",
    f=f2,
    grad=grad_f2,
    x0=np.array([-1.2, 1.0]),
    alpha=0.003,
    betas=[0.0, 0.90, 0.95],
    max_iter=5000,
    optimum=np.array([1.0, 1.0])
)

plot_rosenbrock_trajectory(experiments_f2)

plot_convergence(
    experiments=experiments_f2,
    title="Function 2: Rosenbrock Convergence"
)

# -------------------------
# Function 3: Own function
# -------------------------

experiments_f3 = run_experiment(
    function_name="f3_own_function",
    f=f3,
    grad=grad_f3,
    x0=np.array([2.0, 2.0]),
    alpha=0.035,
    betas=[0.0, 0.80, 0.98],
    max_iter=200,
    optimum=np.array([0.0, 0.0])
)

plot_trajectory(
    f=f3,
    experiments=experiments_f3,
    x_range=(-2.5, 2.5),
    y_range=(-2.5, 2.5),
    title="Function 3: Own Ill-Conditioned Quadratic",
    optimum=np.array([0.0, 0.0]),
    log_contour=False
)

plot_convergence(
    experiments=experiments_f3,
    title="Function 3: Convergence"
)


# =========================
# 5. Print summary table
# =========================

summary = pd.DataFrame(summary_rows)
print(summary)