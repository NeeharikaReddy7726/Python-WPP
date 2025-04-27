import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-5*x+6  # root at sqrt(2)

# Define the bisection method
def bisection_method(func,iteratn=20 ,tol=1e-5):
    while True:
        a=np.random.uniform(-10,10)
        b=np.random.uniform(-10,10)

        if func(a) * func(b) < 0:
            break
    
    # Array to store updates (intervals and midpoints)
    updates = []

    for i in range(iteratn):
        c = (a + b) / 2  # Midpoint
        updates.append([a, b, c, func(c)])  # Save current values

        if abs(func(c)) < tol:  # Check if the root is found
            break
        elif func(a) * func(c) < 0:  # Root lies between a and c
            b = c
        else:  # Root lies between c and b
            a = c

    return np.array(updates), c

# Example usage
updates,root=bisection_method(f)

iterations=np.arange(len(updates))
midpoints=updates[:,2]
 
plt.plot(iterations,midpoints,marker='o')
plt.xlabel("Number of iterations")
plt.ylabel("Midpoints")
plt.title('Convergence of Midpoint to Root (Bisection Method)')
plt.grid(True)
plt.show()

print(f"The approximate root is: {root}")