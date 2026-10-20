
import numpy as np
import matplotlib.pyplot as plt

# Function
def f(x):
    return np.sin(x)

# Repeat for different numbers of data points
for n in [10, 100, 1000]:

    # Step 1: Generate data points
    x = np.linspace(0, 4*np.pi, n)
    y = f(x)
    h = x[1] - x[0]

    # Step 2: Differentiation
    forward = []
    backward = []
    central = []

    for i in range(n-1):
        forward.append((y[i+1]-y[i])/h)
        backward.append((y[i+1]-y[i])/h)

    for i in range(1, n-1):
        central.append((y[i+1]-y[i-1])/(2*h))

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

    # Step 5: Plot the function
    plt.figure()
    plt.plot(x, y, label="sin(x)")
    plt.scatter(x, y, s=10, label="Data points")
    plt.title("Function, n = " + str(n))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()

    # Step 6: Plot the derivatives
    plt.figure()
    plt.plot(x, np.cos(x), label="Exact derivative")
    plt.plot(x[:-1], forward, label="Forward difference")
    plt.plot(x[1:], backward, label="Backward difference")
    plt.plot(x[1:-1], central, label="Central difference")
    plt.title("Differentiation, n = " + str(n))
    plt.xlabel("x")
    plt.ylabel("Derivative")
    plt.legend()
    plt.grid()

    # Step 7: Plot the integrals
    plt.figure()
    plt.plot(x[1:], L, label="Left rectangle")
    plt.plot(x[1:], R, label="Right rectangle")
    plt.plot(x[1:], M, label="Midpoint method")
    plt.plot(x[1:], 1-np.cos(x[1:]), "--",
             label="Exact integral")
    plt.title("Integration, n = " + str(n))
    plt.xlabel("x")
    plt.ylabel("Integral from 0 to x")
    plt.legend()
    plt.grid()

    plt.show()
