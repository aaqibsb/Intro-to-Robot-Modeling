# Program to trace a circle with a Force on end-effector(using second method for Jacobian) with Franka Emika Panda Cobot
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=False, wrap_line=False)

""" Defining gravity and mass of links """
m1 = 4.971
m2 = 0.647
m4 = 6.815
m5 = 1.226
m6 = 1.667
m7 = 0.736
g = 9.81

""" Defining the transformation matrix """
def transformation(al, th, d, a):
    t = Matrix([[cos(th), -sin(th) * cos(al),  sin(th) * sin(al), a * cos(th)],
                [sin(th),  cos(th) * cos(al), -cos(th) * sin(al), a * sin(th)],
                [      0,            sin(al),            cos(al),           d],
                [      0,                  0,                  0,           1]])
    return t


""" Defining joint angles as symbols """
q1_s = Symbol('\u0398\u2081')
q2_s = Symbol('\u0398\u2082')
q4_s = Symbol('\u0398\u2084')
q5_s = Symbol('\u0398\u2085')
q6_s = Symbol('\u0398\u2086')
q7_s = Symbol('\u0398\u2087')

""" Defining DH parameters """
alpha = [pi / 2, -pi / 2, -pi / 2, pi / 2, pi / 2, -pi / 2, 0]
theta = [q1_s, q2_s, 0, q4_s, q5_s, q6_s, q7_s]
di = [0.3330, 0, 0.3160, 0, 0.3840, 0, -0.2070]
ai = [0, 0, 0.0880, -0.0880, 0, 0.0880, 0]

""" Defining transformation matrices """
T1 = transformation(alpha[0], theta[0], di[0], ai[0])
T2 = transformation(alpha[1], theta[1], di[1], ai[1])
T3 = transformation(alpha[2], theta[2], di[2], ai[2])
T4 = transformation(alpha[3], theta[3], di[3], ai[3])
T5 = transformation(alpha[4], theta[4], di[4], ai[4])
T6 = transformation(alpha[5], theta[5], di[5], ai[5])
T7 = transformation(alpha[6], theta[6], di[6], ai[6])

""" Defining transformation matrices wrt zeroth frame """
H1 = T1
H2 = H1 * T2
H3 = H2 * T3 * T4
H4 = H3 * T5
H5 = H4 * T6
H6 = H5 * T7

""" Extracting Z matrix from each homogeneous transformation matrices """
Z0 = Matrix([[0], [0], [1]])
Z1 = Matrix([[H1[2]], [H1[6]], [H1[10]]])
Z2 = Matrix([[H2[2]], [H2[6]], [H2[10]]])
Z3 = Matrix([[H3[2]], [H3[6]], [H3[10]]])
Z4 = Matrix([[H4[2]], [H4[6]], [H4[10]]])
Z5 = Matrix([[H5[2]], [H5[6]], [H5[10]]])
Z6 = Matrix([[H6[2]], [H6[6]], [H6[10]]])

""" Extracting final end-effector position from the last transformation matrix """
Xp = Matrix([[H6[3]], [H6[7]], [H6[11]]])

""" Differentiating Xp matrix with theta1, theta2, theta4, theta5, theta6, theta7 """
C1 = diff(Xp, q1_s)
C2 = diff(Xp, q2_s)
C3 = diff(Xp, q4_s)
C4 = diff(Xp, q5_s)
C5 = diff(Xp, q6_s)
C6 = diff(Xp, q7_s)

""" Defining components of Jacobian matrix """
J1 = Matrix([[C1], [Z1]])
J2 = Matrix([[C2], [Z2]])
J3 = Matrix([[C3], [Z3]])
J4 = Matrix([[C4], [Z4]])
J5 = Matrix([[C5], [Z5]])
J6 = Matrix([[C6], [Z6]])

""" Setting up final Jacobian matrix """
J_s = Matrix([[J1, J2, J3, J4, J5, J6]])
# pprint(J_s)

""" Defining initial joint angles """
q1 = 0
q2 = 0
q4 = pi / 2
q5 = 0
q6 = pi
q7 = 0

""" Force matrix """
F = Matrix([[-5], [0], [0], [0], [0], [0]])

""" Torques """
Torc1 = []
Torc2 = []
Torc4 = []
Torc5 = []
Torc6 = []
Torc7 = []

""" Calculating Gravity matrix elements """
P1 = Matrix([C1.transpose()]) * Matrix([[0], [0], [-m1 * g]])
P2 = Matrix([C2.transpose()]) * Matrix([[0], [0], [-m2 * g]])
P3 = Matrix([C3.transpose()]) * Matrix([[0], [0], [-m4 * g]])
P4 = Matrix([C4.transpose()]) * Matrix([[0], [0], [-m5 * g]])
P5 = Matrix([C5.transpose()]) * Matrix([[0], [0], [-m6 * g]])
P6 = Matrix([C6.transpose()]) * Matrix([[0], [0], [-m7 * g]])

""" Setting up gravity matrix """
P = Matrix([[-P1], [-P2], [-P3], [-P4], [-P5], [-P6]])
print("Gravity Matrix:")
pprint(P)

theta_arr = np.linspace(90, 450, num=100)
dt = 200/100
for t in theta_arr:
    """ Defining components of X_dot matrix """
    Vx = 0                                                  # Derivative of x = 0.679 wrt time
    Vy = -0.1 * 2 * (pi / 200) * sin(t * (pi / 180))        # Derivative of y = r*cosθ wrt time
    Vz = 0.1 * 2 * (pi / 200) * cos(t * (pi / 180))         # Derivative of z = r*sinθ wrt time
    Wx = 0                                                  # Angular velocity of end effector in x direction
    Wy = 0                                                  # Angular velocity of end effector in y direction
    Wz = 0                                                  # Angular velocity of end effector in z direction

    """ Setting up X_dot matrix """
    X_dot = Matrix([[Vx], [Vy], [Vz], [Wx], [Wy], [Wz]])

    """ Substituting values of joint angles in Jacobian matrix """
    J = J_s.subs({q1_s: q1, q2_s: q2, q4_s: q4, q5_s: q5, q6_s: q6, q7_s: q7})

    """ Substituting values of joint angles in final transformation matrix """
    H6_1 = H6.subs({q1_s: q1, q2_s: q2, q4_s: q4, q5_s: q5, q6_s: q6, q7_s: q7})

    """ Jacobian Transpose """
    J_T = J.transpose()

    """ Calculating q_dot matrix """
    q_dot = (J.pinv() * X_dot).evalf()

    """ Calculating Torques """
    P_inst = P.subs({q1_s: q1, q2_s: q2, q4_s: q4, q5_s: q5, q6_s: q6, q7_s: q7})
    T = P_inst - J_T*F
    Torc1.append(T[0])
    Torc2.append(T[1])
    Torc4.append(T[2])
    Torc5.append(T[3])
    Torc6.append(T[4])
    Torc7.append(T[5])

    """ Defining elements of q_dot matrix """
    q1_dot = q_dot[0]
    q2_dot = q_dot[1]
    q4_dot = q_dot[2]
    q5_dot = q_dot[3]
    q6_dot = q_dot[4]
    q7_dot = q_dot[5]

    """ Performing numerical integration for each joint angle """
    q1 = q1 + q1_dot * dt
    q2 = q2 + q2_dot * dt
    q4 = q4 + q4_dot * dt
    q5 = q5 + q5_dot * dt
    q6 = q6 + q6_dot * dt
    q7 = q7 + q7_dot * dt

""" Plotting function """
time = np.linspace(0, 200, num=100)
fig, ((ax1, ax2, ax3), (a1, a2, a3)) = plt.subplots(2, 3)
fig.suptitle('Torques of Joints - 1,2,4,5,6,7')

ax1.plot(time, Torc1)
ax1.set_title("Torque 1")
ax1.set(ylabel='N-m')

ax2.plot(time, Torc2)
ax2.set_title("Torque 2")
ax2.sharex(ax1)

ax3.plot(time, Torc4)
ax3.set_title("Torque 4")
ax3.sharex(ax2)
fig.tight_layout()

a1.plot(time, Torc5)
a1.set_title("Torque 5")
a1.set(ylabel='N-m', xlabel='time')
a2.sharey(ax1)

a2.plot(time, Torc6)
a2.set_title("Torque 6")
a2.set(xlabel='time')
a2.sharex(a1)

a3.plot(time, Torc7)
a3.set_title("Torque 7")
a3.set(xlabel='time')
a3.sharex(a2)
fig.tight_layout()


ax1.grid()
ax2.grid()
ax3.grid()
a1.grid()
a2.grid()
a3.grid()
plt.show()
plt.show()
