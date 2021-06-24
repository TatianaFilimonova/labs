from sympy import *
import numpy as np
import math

x, y = symbols('x y')
f1 = sin(x + 0.5) - y - 1
f2 = x + cos(y - 2) - 2

def fun1(x0, y0):
    return math.sin(x0 + 0.5) - y0 - 1

def fun2(x0, y0):
    return x0 + math.cos(y0 - 2) - 2

def dx_fun1(x0, y0):
    return diff(f1, x).subs(x, x0).subs(y, y0).evalf()

def dy_fun1(x0, y0):
    return diff(f1, y).subs(x, x0).subs(y, y0).evalf()

def dx_fun2(x0, y0):
    return diff(f2, x).subs(x, x0).subs(y, y0).evalf()

def dy_fun2(x0, y0):
    return diff(f2, y).subs(x, x0).subs(y, y0).evalf()


x0 = 2
y0 = -1
k = 0

A = np.array([[dx_fun1(x0, y0), dy_fun1(x0, y0)], [dx_fun2(x0, y0), dy_fun2(x0, y0)]], dtype='float')
B = np.array([(-1) * fun1(x0, y0), (-1) * fun2(x0, y0)], dtype='float')
X = np.linalg.solve(A, B)
delta_x = X[0]
delta_y = X[1]
x0 += delta_x
y0 += delta_y
#print(f'x{k}: {x0} y{k}: {y0}')
k += 1

while abs(delta_x) >= pow(10, -4):
    A = np.array([[dx_fun1(x0, y0), dy_fun1(x0, y0)], [dx_fun2(x0, y0), dy_fun2(x0, y0)]], dtype='float')
    B = np.array([(-1) * fun1(x0, y0), (-1) * fun2(x0, y0)], dtype='float')
    X = np.linalg.solve(A, B)
    delta_x = X[0]
    delta_y = X[1]
    x0 = x0 + delta_x
    y0 = y0 + delta_y
#    print(f'x{k}: {x0} y{k}: {y0}')
    k += 1
print(f'x = {x0}; y = {y0}')
