
import numpy as np
import matplotlib.pyplot as plt

# 1. Known function
def f(x):
    return np.sin(x)

# 2. Equally spaced and unequally spaced data
x = np.array([0., 1., 2., 3.])
y = f(x)

a = np.array([0., 0.7, 1.8, 3.])
b = f(a)

# 3. Newton forward and backward formulas
def newton(x, y, z, backward=False):
    h = x[1] - x[0]

    # Calculate differences manually
    d1 = [y[i+1]-y[i] for i in range(3)]
    d2 = [d1[i+1]-d1[i] for i in range(2)]
    d3 = d2[1]-d2[0]

    if not backward:
        u = (z-x[0])/h
        p = (y[0] + u*d1[0]
             + u*(u-1)*d2[0]/2
             + u*(u-1)*(u-2)*d3/6)
    else:
        u = (z-x[-1])/h
        p = (y[-1] + u*d1[-1]
             + u*(u+1)*d2[-1]/2
             + u*(u+1)*(u+2)*d3/6)

    return p

# 4. Newton divided difference
def divided(x, y, z):
    c = list(y)

    for j in range(1, len(x)):
        for i in range(len(x)-1, j-1, -1):
            c[i] = (c[i]-c[i-1])/(x[i]-x[i-j])

    p = c[-1]
    for i in range(len(x)-2, -1, -1):
        p = p*(z-x[i]) + c[i]

    return p

# 5. Lagrange interpolation
def lagrange(x, y, z):
    p = 0

    for i in range(len(x)):
        term = y[i]
        for j in range(len(x)):
            if i != j:
                term *= (z-x[j])/(x[i]-x[j])
        p += term

    return p

# 6. Calculate interpolation errors
print("Actual and interpolated values")

for t in [0.5, 1.5, 2.5]:
    actual = f(t)
    print(f"\nx = {t}, Actual = {actual:.5f}")

    for name, p in [
        ("Forward", newton(x,y,t)),
        ("Backward", newton(x,y,t,True)),
        ("Divided Difference", divided(a,b,t)),
        ("Lagrange", lagrange(a,b,t))
    ]:
        print(name, f"Value = {p:.5f}",
              f"Error = {abs(actual-p):.6f}")

# 7. Plot interpolation and error
z = np.linspace(-1, 5, 200)

forward = np.array([newton(x,y,t) for t in z])
backward = np.array([newton(x,y,t,True) for t in z])
dd = np.array([divided(a,b,t) for t in z])
lag = np.array([lagrange(a,b,t) for t in z])

fig, ax = plt.subplots(2, 1, figsize=(9, 8))

# Interpolation plot
ax[0].plot(z, f(z), label="Actual sin(x)")
ax[0].plot(z, forward, label="Newton Forward")
ax[0].plot(z, backward, label="Newton Backward")
ax[0].plot(z, dd, label="Divided Difference")
ax[0].plot(z, lag, label="Lagrange")

ax[0].plot(x, y, 'ko', markersize=7, label="Equal-spaced points")
ax[0].plot(a, b, 'k^', markersize=7, label="Unequal-spaced points")
ax[0].set_ylabel("f(x)")
ax[0].set_title("Polynomial Interpolation")
ax[0].legend(fontsize=8)
ax[0].grid()

# Absolute error plot
ax[1].plot(z, abs(f(z)-forward), label="Forward Error")
ax[1].plot(z, abs(f(z)-backward), label="Backward Error")
ax[1].plot(z, abs(f(z)-dd), label="Divided Difference Error")
ax[1].plot(z, abs(f(z)-lag), label="Lagrange Error")

ax[1].set_xlabel("x")
ax[1].set_ylabel("Absolute Error")
ax[1].set_title("Interpolation Error")
ax[1].legend(fontsize=8)
ax[1].grid()

plt.tight_layout()
plt.show()



