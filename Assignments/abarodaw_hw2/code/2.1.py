# Program to plot the Si, Theta, Fi, Wx, Wy, Wz with respect to global frame
from sympy import *
from mpmath import radians, degrees
import numpy as np
from matplotlib import pyplot as plt

init_printing(use_unicode=True, wrap_line=False)

Si = radians(35)
T = radians(15)
Fi = radians(20)
Si_m = []
T_m = []
Fi_m = []
W_x = []
W_y = []
W_z = []

""" Defining Rotation Matrix of Euler angles """
Rz = Matrix([[cos(Fi), -sin(Fi), 0],
             [sin(Fi),  cos(Fi), 0],
             [      0,        0, 1]])

Ry = Matrix([[ cos(T), 0, sin(T)],
             [      0, 1,      0],
             [-sin(T), 0, cos(T)]])

Rx = Matrix([[1,       0,        0],
             [0, cos(Si), -sin(Si)],
             [0, sin(Si), cos(Si)]])

Rot = Rz * Ry * Rx
print("Rotation Matrix:")
pprint(Rot)
print('\n')

Theta = acos((Trace(Rot).simplify() - 1) / 2)
print("Equivalent angle \u03B8: ", Theta, "\n")

print("Equivalent axis K vector: ")
K = 1 / (2 * sin(Theta)) * Matrix([[Rot[2, 1] - Rot[1, 2]],
                                   [Rot[0, 2] - Rot[2, 0]],
                                   [Rot[1, 0] - Rot[0, 1]]])
pprint(K)
print("\n")

Kx = K[0, 0]
Ky = K[1, 0]
Kz = K[2, 0]

""" Calculating Wx Wy Wz """
Wx = radians(1)                                 # Converting 1 deg/s to rad/s
Theta_dot = Wx/Kx
Wy = Theta_dot*Ky
Wz = Theta_dot*Kz

""" Wx Wy Wz """
print("Wx:", Wx, "rad/s")
print("Wy:", Wy, "rad/s")
print("Wz:", Wz, "rad/s")

""" Shortest Time """
Time = Theta/Theta_dot
print("Shortest Time:", Time, "seconds")


t = 0
T1 = np.arange(0.0, Time, 0.1)
for t in T1:
    V = 1 - cos(Theta_dot*t)

    """ Defining the rotation matrix elements of axis-angle representation """
    K11 = ((Kx**2)*V) + cos(Theta_dot*t)
    # K12 = (Kx*Ky*V) - Kz*sin(t)
    # K13 = (Kx*Kz*V) + Ky*sin(Theta_dot*t)
    K21 = (Kx*Ky*V) + Kz*sin(Theta_dot*t)
    # K22 = (Ky**2)*V + cos(t)
    # K23 = (Ky*Kz*V) - (Kx*sin(Theta_dot*t))
    K31 = (Kx*Kz*V) - (Ky*sin(Theta_dot*t))
    K32 = (Ky*Kz*V) + (Kx*sin(Theta_dot*t))
    K33 = ((Kz**2)*V) + cos(Theta_dot*t)

    # Rkt = Matrix([[K11, K12, K13],
    #               [K21, K22, K23],
    #               [K31, K32, K33]])

    """ Finding the Euler Angles """
    Si = atan2(K32, K33)
    T = atan2(-K31, sqrt(K32**2 + K33**2))
    Fi = atan2(K21, K11)

    """ Storing the values in a matrix for plotting """
    Si_m.append(degrees(Si))
    T_m.append(degrees(T))
    Fi_m.append(degrees(Fi))

    W_x.append(degrees(Wx))
    W_y.append(degrees(Wy))
    W_z.append(degrees(Wz))

""" Plotting Function """
fig, ((ax1, ax2, ax3), (a1, a2, a3)) = plt.subplots(2, 3)
fig.suptitle('Euler angles & Angular Velocity')

ax1.plot(T1, Si_m)
ax1.set_title("\u03A8")
ax1.set(ylabel='degrees')

ax2.plot(T1, T_m)
ax2.set_title("\u03B8")
ax2.sharex(ax1)

ax3.plot(T1, Fi_m)
ax3.set_title("\u03A6")
ax3.sharex(ax2)
fig.tight_layout()

a1.plot(T1, W_x)
a1.set_title("Wx")
a1.set(ylabel='deg/s', xlabel='time')
a2.sharey(ax1)

a2.plot(T1, W_y)
a2.set_title("Wy")
a2.set(xlabel='time')
a2.sharex(a1)

a3.plot(T1, W_z)
a3.set_title("Wz")
a3.set(xlabel='time')
a3.sharex(a2)
fig.tight_layout()


""" Plotting """
ax1.grid()
ax2.grid()
ax3.grid()
a1.grid()
a2.grid()
a3.grid()
plt.show()

