# Program to trace a circle (using second method for Jacobian) with Franka Emika Panda Cobot
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

""" Defining the transformation matrix """
def transformation(al, th, d, a):
    t = Matrix([[cos(th), -sin(th) * cos(al),  sin(th) * sin(al), a * cos(th)],
                [sin(th),  cos(th) * cos(al), -cos(th) * sin(al), a * sin(th)],
                [      0,            sin(al),            cos(al),           d],
                [      0,                  0,                  0,           1]])
    return t


""" Defining joint angles as symbols """
q1_s = Symbol('theta1')
q2_s = Symbol('theta2')
q4_s = Symbol('theta4')
q5_s = Symbol('theta5')
q6_s = Symbol('theta6')
q7_s = Symbol('theta7')

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
print("J :")
pprint(J_s)

""" Defining initial joint angles """
q1 = 0
q2 = 0
q4 = pi / 2
q5 = 0
q6 = pi
q7 = 0

""" Plotting function """
circle = plt.figure(figsize=(4, 4))
trajectory = circle.add_subplot(111, projection='3d')
plt.xlim(0, 1)                                              # X-axis limit
plt.ylim(-0.15, 0.15)                                       # Y-axis limit

trajectory.set_xlabel('X-axis')
trajectory.set_ylabel('Y-axis')
trajectory.set_zlabel('Z-axis')
trajectory.set_title('Trajectory of End-Effector')

time = np.linspace(90, 450, num=50)
dt = 5 / 50
for t in time:
    """ Defining components of X_dot matrix """
    Vx = 0                                                  # Derivative of x = 0.679 wrt time
    Vy = -0.1 * 2 * (pi / 5) * sin(t * (pi / 180))          # Derivative of y = r*cosθ wrt time
    Vz = 0.1 * 2 * (pi / 5) * cos(t * (pi / 180))           # Derivative of z = r*sinθ wrt time
    Wx = 0                                                  # Angular velocity of end effector in x direction
    Wy = 0                                                  # Angular velocity of end effector in y direction
    Wz = 0                                                  # Angular velocity of end effector in z direction

    """ Setting up X_dot matrix """
    X_dot = Matrix([[Vx], [Vy], [Vz], [Wx], [Wy], [Wz]])

    """ Substituting values of joint angles in Jacobian matrix """
    J = J_s.subs({q1_s: q1, q2_s: q2, q4_s: q4, q5_s: q5, q6_s: q6, q7_s: q7})

    """ Substituting values of joint angles in final transformation matrix """
    H6_1 = H6.subs({q1_s: q1, q2_s: q2, q4_s: q4, q5_s: q5, q6_s: q6, q7_s: q7})

    """ Plotting """
    trajectory.scatter(0.679, H6_1[7], H6_1[11])
    plt.pause(0.5)

    """ Calculating q_dot matrix """
    q_dot = (J.pinv() * X_dot).evalf()

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

plt.show()
