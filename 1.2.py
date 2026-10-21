import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Function
def f(x):
    return np.sin(x)
def H(x):
    return np.cos(x)

# Repeat for different numbers of data points
for n in [10, 100, 1000]:

    # Step 1: Generate data points
    x = np.linspace(np.pi/2, 5*np.pi, n)
    y = f(x)
    h = x[1] - x[0]

    # Step 2: Differentiation
    forward = []
    backward = []
    central = []

 

    # Forward difference
    for i in range(n-1):
        forward.append((y[i+1] - y[i]) / h)

    # Backward difference
    for i in range(1, n):
        backward.append((y[i] - y[i-1]) / h)

    # Central difference
    for i in range(1, n-1):
        central.append((y[i+1] - y[i-1]) / (2*h))

    # Step 3: Integration using area methods
    left = 0
    right = 0
    mid = 0

    L, R, M = [], [], []

    for i in range(n-1):
        left += y[i]*h
        right += y[i+1]*h
        midpoint = (x[i]+x[i+1])/2
        mid += f(midpoint)*h

        L.append(left)
        R.append(right)
        M.append(mid)

    # Step 4: Compare with exact results
    exact_area = 1 - np.cos(4*np.pi)

    print("\nNumber of points:", n)
    print("Step size:", h)
    print("Exact integral:", exact_area)
    print("Left rectangle:", left,
          "Error:", abs(exact_area-left))
    print("Right rectangle:", right,
          "Error:", abs(exact_area-right))
    print("Midpoint method:", mid,
          "Error:", abs(exact_area-mid))
    # For Radian Grph
    def set_pi_ticks(ax, x):
        step = np.pi / 2

        ticks = np.arange(
            np.ceil(x[0] / step),
            np.floor(x[-1] / step) + 1
        ) * step

        labels = []
        for t in ticks:
            k = round(t / step)

            if k == 0:
                labels.append("0")
            elif k % 2 == 0:
                labels.append(rf"${k // 2}\pi$")
            else:
                labels.append(rf"${k}\pi/2$")

        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)
        ax.set_xlim(x[0], x[-1])

    # Step 5: Plot the function
    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.scatter(x, y, s=10, label="Data points")
    ax.set_title(f"Function, n = {n}")
    ax.set_xlabel("x (radians)")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid()
    set_pi_ticks(ax, x)

    # Step 6: Plot derivatives
    fig, ax = plt.subplots()
    ax.plot(x, np.cos(x), label="Exact derivative")
    ax.plot(x[:-1], forward, label="Forward difference")
    ax.plot(x[1:], backward, label="Backward difference")
    ax.plot(x[1:-1], central, label="Central difference")
    ax.set_title(f"Differentiation, n = {n}")
    ax.set_xlabel("x (radians)")
    ax.set_ylabel("Derivative")
    ax.legend()
    ax.grid()
    set_pi_ticks(ax, x)
    # Step 7: Plot integrals
    fig, ax = plt.subplots()
    ax.plot(x[1:], L, label="Left rectangle")
    ax.plot(x[1:], R, label="Right rectangle")
    ax.plot(x[1:], M, label="Midpoint method")
    ax.plot(
        x[1:],
        np.cos(x[0]) - np.cos(x[1:]),
        "--",
        label="Exact integral"
    )
    ax.set_title(f"Integration, n = {n}")
    ax.set_xlabel("x (radians)")
    ax.set_ylabel("Integral from a to x")
    ax.legend()
    ax.grid()
    set_pi_ticks(ax, x)
plt.show()
  
