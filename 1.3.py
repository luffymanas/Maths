
import numpy as np
import matplotlib.pyplot as plt

# Example 1: x^2 - 4 = 0
def f1(x):
    return x**2 - 4

def df1(x):
    return 2*x

# Example 2: x^3 - x^2 + 4x - 4 = 0
def f2(x):
    return x**3 - x**2 + 4*x - 4

def df2(x):
    return 3*x**2 - 2*x + 4

# Bisection method
def bisection(f, a, b):
    for i in range(100):
        c = (a+b)/2

        if abs(f(c)) < 1e-8:
            return c

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return (a+b)/2

# Newton-Raphson method
def newton(f, df, x):
    for i in range(100):
        x1 = x - f(x)/df(x)

        if abs(x1-x) < 1e-8:
            return x1

        x = x1

    return x

# Calculate roots
print("Example 1: x^2 - 4 = 0")
print("Bisection root:", bisection(f1, 0, 3))
print("Newton-Raphson root:", newton(f1, df1, 3))
print("Negative root:", newton(f1, df1, -3))

print("\nExample 2: x^3 - x^2 + 4x - 4 = 0")
print("Bisection root:", bisection(f2, 0, 2))
print("Newton-Raphson root:", newton(f2, df2, 2))

# Plot the polynomials
x = np.linspace(-3, 3, 400)

plt.plot(x, f1(x), label="x^2 - 4")
plt.plot(x, f2(x), label="x^3 - x^2 + 4x - 4")
plt.axhline(0, color="black")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Polynomial Roots")
plt.legend()
plt.grid()
plt.show()
