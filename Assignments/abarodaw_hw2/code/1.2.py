# Program to define the position of the drone and output the area covered by the camera on the ground
from sympy import *

init_printing(use_unicode=True, wrap_line=False)


""" Taking inputs """
x, y = symbols('x y')
Si = float(input("Enter rotation about X axis (\u03A8): "))
T = float(input("Enter rotation about Y axis (\u03B8): "))
Fi = float(input("Enter rotation about Z axis (\u03A6): "))
dx = float(input("Enter displacement wrt X axis (dx): "))
dy = float(input("Enter displacement wrt Y axis (dy): "))
dz = float(input("Enter displacement wrt Z axis (dz): "))
# print(T, Fi, Si)

""" Defining the Rotation Matrix """
Rz = Matrix([[cos(Fi), -sin(Fi), 0],
             [sin(Fi),  cos(Fi), 0],
             [      0,        0, 1]])

Ry = Matrix([[ cos(T),   0, sin(T)],
             [      0,   1,      0],
             [-sin(T),   0, cos(T)]])

Rx = Matrix([[1,        0,        0],
             [0,  cos(Si), -sin(Si)],
             [0,  sin(Si), cos(Si)]])

R = Rz*Ry*Rx
# pprint(R)

""" Defining Homogeneous Transformation Matrix """
# Attached negative signs to orient the body frame with the global frame
H = Matrix([[-R[0, 0], R[0, 1], -R[0, 2],  dx],
            [-R[1, 0], R[1, 1], -R[1, 2], -dy],
            [-R[2, 0], R[2, 1], -R[2, 2],  dz],
            [      0,       0,       0,    1]])

""" Setting equation of ellipse in matrix form """
X = Matrix([[x, y, 0, 1]])
A = H * Transpose(X)

S = Matrix([[1, 0,  0, 0],
            [0, 1,  0, 0],
            [0, 0, -1, 0],
            [0, 0,  0, 0]])
Equation = Transpose(A)*S*A

print('------------------------------------------------')
print("Equation of coverage area:")
pprint(Eq(expand(Equation[0]), 0))
print('------------------------------------------------')

""" Taking Coefficients from the equation """
collected = simplify((factor(Equation[0])))
# print(collected)

x_2 = collected.coeff(x, 2)
a = x_2
# print(x_2)

y_2 = collected.coeff(y, 2)
c = y_2
# print(y_2)

xy = collected.coeff(x*y, 1)
b = xy/2
# print('xy', xy)

collected_x = collected.subs(y, 0)
x_1 = collected_x.coeff(x, 1)
d = x_1/2
# print(x_1)

collected_y = collected.subs(x, 0)
y_1 = collected_y.coeff(y, 1)
e = y_1/2
# print(y_1)

constant = collected.subs({x: 0, y: 0})
f = constant
# print(constant)

""" Calculating area """
coef_matrix = Matrix([[a, b, d],
                      [b, c, e],
                      [d, e, f]])
A = (-3.1416*coef_matrix.det())/pow((a*c-pow(b, 2)), 3/2)
print("Area of the ellipse:", A)
p1 = plot_implicit(Eq(Equation[0], 0), y_var=(y, -10, 10), x_var=(x, -10, 10), title="Coverage area of the drone",
                   xlabel="X", ylabel="Y")

