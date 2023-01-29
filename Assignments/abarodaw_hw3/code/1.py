# Program to find the final transformation matrix (Forward Kinematics) of Franka Emika Panda Cobot using DH Parameters
from sympy import *

init_printing(use_unicode=False, wrap_line=False)

# defining symbols for DH parameters
al, th, d, a = symbols('al th d a')

# defining joint angles as symbols
th1, th2, th3, th4, th5, th6, th7 = symbols('\u03B8\u2081 \u03B8\u2082 \u03B8\u2083 \u03B8\u2084 '
                                            '\u03B8\u2085 \u03B8\u2086 \u03B8\u2087')

# defining link offsets and link lengths as symbols
d1, d3, d5, d7, a3 = symbols('d1 d3 d5 d7 a3')

# setting up Transformation matrices for multiplication
Rz = Matrix([[cos(th), -sin(th), 0, 0],
             [sin(th),  cos(th), 0, 0],
             [      0,        0, 1, 0],
             [      0,        0, 0, 1]])

Tz = Matrix([[  1,  0,  0,  0],
             [  0,  1,  0,  0],
             [  0,  0,  1,  d],
             [  0,  0,  0,  1]])

Tx = Matrix([[  1,  0,  0,  a],
             [  0,  1,  0,  0],
             [  0,  0,  1,  0],
             [  0,  0,  0,  1]])

Rx = Matrix([[  1,        0,        0,  0],
             [  0,  cos(al), -sin(al),  0],
             [  0,  sin(al),  cos(al),  0],
             [  0,        0,        0,  1]])


# defining symbolic expressions of transformations for each row of DH-parameter
result1 = Rz*Tz*Tx*Rx
result2 = Rz*Tz*Tx*Rx
result3 = Rz*Tz*Tx*Rx
result4 = Rz*Tz*Tx*Rx
result5 = Rz*Tz*Tx*Rx
result6 = Rz*Tz*Tx*Rx
result7 = Rz*Tz*Tx*Rx

print("A :")
pprint(result1)
print('\n')

# defining DH parameters
alpha = [pi/2, -pi/2, -pi/2, pi/2, pi/2, -pi/2, 0]
theta = [th1, th2, th3, th4, th5, th6, th7]
di = [ 0.3330, 0, 0.3160, 0, 0.3840, 0, -0.1070]
ai = [ 0, 0, 0.0880, -0.0880, 0, 0.0880, 0]

# substituting each row of DH parameters in their respective expression
result1 = result1.subs(al, alpha[0]).subs(th, theta[0]).subs(d, di[0]).subs(a, ai[0])
result2 = result2.subs(al, alpha[1]).subs(th, theta[1]).subs(d, di[1]).subs(a, ai[1])
result3 = result3.subs(al, alpha[2]).subs(th, theta[2]).subs(d, di[2]).subs(a, ai[2])
result4 = result4.subs(al, alpha[3]).subs(th, theta[3]).subs(d, di[3]).subs(a, ai[3])
result5 = result5.subs(al, alpha[4]).subs(th, theta[4]).subs(d, di[4]).subs(a, ai[4])
result6 = result6.subs(al, alpha[5]).subs(th, theta[5]).subs(d, di[5]).subs(a, ai[5])
result7 = result7.subs(al, alpha[6]).subs(th, theta[6]).subs(d, di[6]).subs(a, ai[6])

print("T1 :")
pprint(result1)
print('\n')

print("T2 :")
pprint(result2)
print('\n')

print("T3 :")
pprint(result3)
print('\n')

print("T4 :")
pprint(result4)
print('\n')

print("T5 :")
pprint(result5)
print('\n')

print("T6 :")
pprint(result6)
print('\n')

print("T7 :")
pprint(result7)
print('\n')

print("T :")
pprint(result1*result2*result3*result4*result5*result6*result7)

