from math import *
from sympy import *

x, y = symbols('x y')
def fun(x):
    return log10(x) - 7 / (2 * x + 6)

def der(x):
    return 14 / (2 * x + 6)**2 + 1/(x*(log(10)))
#    return diff(fun(x))

N = 2
def localisation(a, b, N):
    x0 = a
    x1 = a + (b - a) / N
    while fun(x0) * fun(x1) >= 0:
        x0 = x1
        x1 += (b - a) / N
        if x1 == b:
            N *= 2
            x0 = a
            x1 = a + (b - a) / N
    return {"x0": x0, "x1": x1}

def count(x0):
    return float(x0 - float(fun(x0) / (der(x0))))

def newton(interval):
    a = interval["x0"]
    b = interval["x1"]
    x0 = float(b)
    x1 = count(x0)
    while abs(x1 - x0) >= pow(10, -4):
        x0 = x1
        x1 = count(x0)
    return x1

a = float(1 / 3)
b = float(2 / 3)

print('x = ', {newton(localisation(a, b, N))})