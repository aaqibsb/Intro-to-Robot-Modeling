# Program to plot a 2D trajectory of a car
# Assuming constants for x, y, fi, A, W, r, L, T
import numpy as np
import math as m
from matplotlib import pyplot as plt

x = 0                           # Initial pos for x coordinate
y = 0                           # Initial pos for y coordinate
fi = m.radians(20)              # Orientation in degrees (Phi)
A = m.radians(30)               # Steering angle (Alpha)
W = 5                           # Drive speed (Omega)
r = 0.25                        # Radius of Wheels
L = 4                           # Distance between front wheels and rear wheels
T = np.arange(0.0, 30, 0.1)     # Specifying duration of 5 seconds with 0.1 second increment/intervals

X = []                          # Array to store X coordinates
Y = []                          # Array to store Y coordinates

"""
Conventions for angles fi and A:
Anti-clockwise is positive and Clockwise is negative
"""

Us = r*W/(np.cos(A))            # Velocity w.r.t Alpha
fi_dot = (Us/L)*np.sin(A)       # Change in Orientation

for t in T:
    Ux = Us * np.sin(fi+A)      # X_dot
    X.append(x)                 # Storing x values
    x = x + Ux*0.1

    Uy = Us * np.cos(fi+A)      # Y_dot
    Y.append(y)                 # Storing y values
    y = y + Uy*0.1

    fi = fi + fi_dot*0.1

# Plotting X and Y coordinates of the car
plt.plot(X, Y, label='Trajectory', linewidth=1)

plt.title('Trajectory in 2D')
plt.xlabel('X')
plt.ylabel('Y')

plt.legend()
plt.grid()
plt.show()