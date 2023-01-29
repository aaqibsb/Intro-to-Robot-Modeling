# Program to find inverse kinematics of a 3-link manipulator using sympy
from sympy import *

init_printing(use_unicode=False, wrap_line=False)                   # For setting up the best output for my console

""" Using unicode characters to set up subscripts and dots with symbols """
L1, L2, L3 = symbols('L\u2081 L\u2082 L\u2083')                     # Declaring Links as symbols
t = symbols('t')                                                    # Declaring time as symbol
X_dot, Y_dot, Fi_dot = symbols('X\u0307 Y\u0307 \u03A6\u0307')      # Declaring X_dot, Y_dot, Fi_dot as symbols

X = Function('X\u0307')(t)                                          # Declaring X as function of time
Y = Function('Y\u0307')(t)                                          # Declaring Y as function of time
Fi = Function('\u03A6')(t)                                          # Declaring Fi as function of time
T1 = Function('\u0398\u2081')(t)                                    # Declaring Theta-1 as function of time
T2 = Function('\u0398\u2082')(t)                                    # Declaring Theta-2 as function of time
T3 = Function('\u0398\u2083')(t)                                    # Declaring Theta-3 as function of time


X = L1*cos(T1)+L2*cos(T1+T2)+L3*cos(T1+T2+T3)                       # Initializing X with the equation
Y = L1*sin(T1)+L2*sin(T1+T2)+L3*sin(T1+T2+T3)                       # Initializing Y with the equation

print("X & Y are given by:")
pprint("X : {}\n".format(X))                                        # Using pretty print to display X
pprint("Y : {}\n".format(Y))                                        # Using pretty print to display Y
print('\n')

print("Taking Derivatives:")
print(X_dot, ":", end='\n')
pprint(diff(X, t))                                                  # Using pretty print to display X_dot

print('\n')

print(Y_dot, ":", end='\n')
pprint(diff(Y, t))                                                  # Using pretty print to display Y_dot


XT_1 = Derivative(X, T1).doit()                                     # Calculating derivative of X w.r.t Theta1
XT_2 = Derivative(X, T2).doit()                                     # Calculating derivative of X w.r.t Theta2
XT_3 = Derivative(X, T3).doit()                                     # Calculating derivative of X w.r.t Theta3

# pprint(XT_1)
# pprint(XT_2)
# pprint(XT_3)

YT_1 = Derivative(Y, T1).doit()                                     # Calculating derivative of Y w.r.t Theta1
YT_2 = Derivative(Y, T2).doit()                                     # Calculating derivative of Y w.r.t Theta2
YT_3 = Derivative(Y, T3).doit()                                     # Calculating derivative of Y w.r.t Theta3

# pprint(YT_1)
# pprint(YT_2)
# pprint(YT_3)


print("\n\n")

""" A*B=C """
print("Forward Kinematics Matrix(A) is given by:")
A = Matrix([[XT_1, XT_2, XT_3],                                     # Declaring A as the Forward Kinematics Matrix
            [YT_1, YT_2, YT_3],
            [   1,    1,    1]])
pprint(A)                                                           # Using pretty print to display (A) matrix

print("\n\n", "Taking Inverse:\n")
A_inv = A.inv()                                                     # Taking inverse using sympy
pprint(A_inv)                                                       # Using pretty print to display (A) inverse Matrix

""" B=(A^-1)*C """
C = Matrix([[X_dot],                                                # Declaring C as matrix of X_dot,Y_dot & Fi_dot
            [Y_dot],
            [Fi_dot]])
B = Matrix([[T1],                                                   # Declaring B as matrix of Theta-1,Theta-2 & Theta-3
            [T2],
            [T3]])
B = A_inv * C

print("\n\n", "Multiplying with X\u0307 Y\u0307 & \u03A6\u0307, we get \u0398\u2081\u0307, \u0398\u2082\u0307 & "
              "\u0398\u2083\u0307:")
pprint(B)                                                           # Using pretty print to display (B) matrix

print("\n\nWhere \u0398\u2081\u0307:")
pprint(B[0])                                                        # Using pretty print to display Theta-1_dot

print("\n", "\u0398\u2082\u0307:")
pprint(B[1])                                                        # Using pretty print to display Theta-2_dot

print("\n", "\u0398\u2083\u0307:")
pprint(B[2])                                                        # Using pretty print to display Theta-3_dot


