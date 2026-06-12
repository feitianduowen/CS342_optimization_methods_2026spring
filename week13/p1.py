import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x - 0.5) ** 4 + 0.001 * x

def fp(x):
    return 4 * (x - 0.5) ** 3 + 0.001

def fpp(x):
    return 12 * (x - 0.5) ** 2

def newton_iterations(x0, steps=6):
    xs = [x0]
    x = x0

    for _ in range(steps):
        denom = fpp(x)
        if abs(denom) < 1e-12:
            print("Newton method failed: second derivative is too close to zero.")
            break

        x = x - fp(x) / denom
        xs.append(x)

    return np.array(xs)

grid = np.linspace(0, 1, 500)

plt.figure()
plt.plot(grid, f(grid), label="f(x)")

x0 = 0.501
iters = newton_iterations(x0)
valid = iters[(iters >= 0) & (iters <= 1)]

plt.scatter(valid, f(valid), label="Newton iterates inside [0,1]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Newton's Method Can Fail Near x = 0.5")
plt.legend()
plt.show()

print("Newton iterates:", iters)