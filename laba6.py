import matplotlib.pyplot as plt
import numpy as np
from math import sin, acos

def f(theta):
    return pow(theta, 2) + 1 - acos(theta)
    #return pow(theta,2) + sin(10 * theta)

def derivative(f, x):
    dx = 1E-8
    return (f(x + dx) - f(x - dx)) / (2.0 * dx)

def x_next(f, x_n):
    return x_n - (f(x_n) / derivative(f, x_n))

def newtons_method(f, x_n = 1, i = 0, max_iter = 100):
    i = i + 1
    if (i == max_iter):
        return None
    x_n = x_next(f, x_n)
    print("i:",i,"x_n:",x_n,"f(x_n)",f(x_n))
    if (abs(f(x_n)) < 1E-4):
        return x_n
    newtons_method(f, x_n, i, max_iter)

print(newtons_method(f))