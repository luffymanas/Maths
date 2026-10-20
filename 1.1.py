
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Known function
def f(x):
    return np.sin(x)

# Equally spaced data
x = np.array([0., 1., 2., 3.])
y = f(x)

# Unequally spaced data
a = np.array([0., 0.7, 1.8, 3.])
b = f(a)

# Newton forward and backward formulas
def newton(x, y, z, backward=False):
    d = [list(y)]

    # Difference table
    for j in range(1, len(x)):
        d.append([d[j-1][i+1] - d[j-1][i]
                  for i in range(len(x)-j)])

    h = x[1] - x[0]
    u = (z-x[0])/h if not backward else (z-x[-1])/h
    p = y[0] if not backward else y[-1]

    for j in range(1, len(x)):
        term = 1
        for k in range(j):
            term *= u-k if not backward else u+k
        diff = d[j][0] if not backward else d[j][-1]
        p += term*diff/factorial(j)

    return p

# Newton divided difference
def divided(x, y, z):
    c = list(y)

    for j in range(1, len(x)):
        for i in range(len(x)-1, j-1, -1):
            c[i] = (c[i]-c[i-1])/(x[i]-x[i-j])

    p = c[-1]
    for i in range(len(x)-2, -1, -1):
        p = p*(z-x[i]) + c[i]
    return p

# Lagrange formula
def lagrange(x, y, z):
    p = 0
    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if i != j:
                term *= (z-x[j])/(x[i]-x[j])
        p += term
    return p

# Plot all methods

z = np.linspace(-1, 5, 200)

plt.plot(z, f(z), label="Actual sin(x)")
plt.plot(z, [newton(x,y,t) for t in z], label="Forward")
plt.plot(z, [newton(x,y,t,True) for t in z], label="Backward")
plt.plot(z, [divided(a,b,t) for t in z], label="Divided Difference")
plt.plot(z, [lagrange(a,b,t) for t in z], label="Lagrange")

# Visible black data points
plt.plot(x, y, 'ko', markersize=8, label="Equal-spaced points")
plt.plot(a, b, 'k^', markersize=8, label="Unequal-spaced points")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Polynomial Interpolation")
plt.legend()
plt.grid()
plt.show()


# Compare values and errors at x = 1.5
t = 1.5
print("Actual value:", f(t))

for name, value in [
    ("Forward", newton(x,y,t)),
    ("Backward", newton(x,y,t,True)),
    ("Divided Difference", divided(a,b,t)),
    ("Lagrange", lagrange(a,b,t))
]:
    print(name, "Value:", value,
          "Error:", abs(f(t)-value))
