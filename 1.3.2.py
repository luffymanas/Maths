
import numpy as np
import matplotlib.pyplot as plt

# Sun and Earth mass ratio
mu = 5.9722e24 / 1.9885e30

# L1 polynomial: Sun - spacecraft - Earth
def f1(x):
    return x**5 + 3*x**4 + 3*x**3 - 3*mu*x**2 - 3*mu*x - mu

# L2 polynomial: Sun - Earth - spacecraft
def f2(x):
    return (1+mu)*x**5 + (3+2*mu)*x**4 + (3+mu)*x**3 - mu*x**2 - 2*mu*x - mu

# L3 polynomial: spacecraft - Sun - Earth
def f3(x):
    return x**5 + 2*x**4 + x**3 - (1+3*mu)*x**2 - (2+3*mu)*x - (1+mu)

# Bisection method
def bisection(f, a, b):
    for i in range(100):
        c = (a+b)/2

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2

# Find positive roots
X1 = bisection(f1, 0, 1)
X2 = bisection(f2, 0, 1)
X3 = bisection(f3, 0, 2)

# Position relative to the Sun, in AU
L1 = 1 - X1
L2 = 1 + X2
L3 = -1 / X3

AU = 149597870.7  # kilometres

print("Sun-Earth Lagrange Points")
print("Mass ratio =", mu)

for name, root, position in [
    ("L1", X1, L1),
    ("L2", X2, L2),
    ("L3", X3, L3)
]:
    print(f"\n{name}:")
    print("Polynomial root =", root)
    print("Position from Sun (AU) =", position)
    print("Position from Sun (km) =", position*AU)

# Plot the three polynomials

# Plot each polynomial separately

# Plot each polynomial separately
fig, ax = plt.subplots(3, 1, figsize=(8, 10))

for axis, func, root, name in [
    (ax[0], f1, X1, "L1 Polynomial"),
    (ax[1], f2, X2, "L2 Polynomial"),
    (ax[2], f3, X3, "L3 Polynomial")
]:
    xx = np.linspace(max(0, root-0.1), root+0.1, 500)
    axis.plot(xx, [func(t) for t in xx], label=name)
    axis.axhline(0, color="gray")
    axis.scatter(root, func(root), color="black", zorder=5)
    axis.set_title(f"{name}: Root = {root:.6f}")
    axis.set_xlabel("X")
    axis.set_ylabel("f(X)")
    axis.grid()
    axis.legend()

plt.tight_layout()
plt.show()

# Fourth plot: All three polynomials together
plt.figure(figsize=(9, 6))

for func, root, name in [
    (f1, X1, "L1"),
    (f2, X2, "L2"),
    (f3, X3, "L3")
]:
    xx = np.linspace(max(0, root-0.1), root+0.1, 500)
    plt.plot(xx, [func(t) for t in xx], label=name)
    plt.plot(root, func(root), "ko")

plt.axhline(0, color="gray")
plt.xlabel("X")
plt.ylabel("Polynomial value")
plt.title("All Three Lagrange Point Polynomials")
plt.legend()
plt.grid()
plt.show()

