from cmath import inf
import numpy as np
import math
import time
import threading
from sympy import *


def gradientDescentFx(a, b, c, d):
    x = Symbol('x')
    f = a*x**3+b*x**2+c*x+d
    f_prime = f.diff(x)
    f_prime = lambdify(x, f_prime)
    eps = 0.000001

    x_curr = 0.5
    iterations = 5000
    learning_rate = 0.01
    start_time = time.time()
    print("Starting computation of gradient descent")
    for i in range(iterations):
        x_new = x_curr - learning_rate * f_prime(x_curr)
        if (abs(x_new - x_curr < eps)):
            break
        if (time.time() - start_time > 1):
            break
        x_curr = x_new
    print(x_curr)
    print(i)
    print("--- %s seconds ---" % (time.time() - start_time))


def gradientDescentGx(A, b, c, x):
    eps = 0.00000000001
    iterations = 1000000
    learning_rate = 0.01
    start_time = time.time()
    print("Starting computation of gradient descent")
    for i in range(iterations):
        grad = np.add(np.dot(np.add(A, np.transpose(A)), x), b)
        x_new = x - np.multiply(grad, learning_rate)
        if ((x[0][0]-x_new[0][0] < eps and x[1][0]-x_new[1][0] < eps) or (time.time() - start_time) > 1):
            break
        x = x_new
    Gx = c + np.dot(np.transpose(b), x) + \
        np.dot(np.dot(np.transpose(x), A), x)
    print(x)
    print(Gx)
    print(i)
    print("--- %s seconds ---" % (time.time() - start_time))


c = 5
b = np.array([[-2], [1]])
A = np.array([[2, -1], [-1, 2]])
x = np.array([[10], [4]])

gradientDescentGx(A, b, c, x)

# print(x[1][0])

gradientDescentFx(0.5, -5, 2, -3)
