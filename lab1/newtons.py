from cmath import inf
import numpy as np
import math
import time
import threading
from sympy import *


def newtonsFx(a, b, c, d, start):
    x = Symbol('x')
    y = Symbol('y')
    f = a*x**3+b*x**2+c*x+d
    f_prime = f.diff(x)
    f_prime = lambdify(x, f_prime)
    eps = 0.000001

    f = lambdify(x, f)

    x_curr = start
    iterations = 5000
    start_time = time.time()

    print("Starting computation of Newtons")

    for i in range(iterations):
        x_curr = x_curr - f(x_curr)/f_prime(x_curr)
        if (abs(f(x_curr)) < eps):
            break
        if (time.time() - start_time > 1):
            break
    print(x_curr)
    print(i)
    print("--- %s seconds ---" % (time.time() - start_time))


def newtonsGx(A, b, c, x):
    eps = 0.00000000001
    iterations = 30
    start_time = time.time()

    print("Starting computation of Newtons")
    for i in range(iterations):
        f_curr = np.add(np.dot(np.add(A, np.transpose(A)), x), b)

        f_prime = np.add(np.transpose(A), A)

        x = x - np.divide(f_curr, f_prime)

        print(f_prime)

        if (abs(np.all(f_prime)) < eps or (time.time() - start_time > 1)):
            print('breaking')
            break

    # print(x)
    # print(i)
    print("--- %s seconds ---" % (time.time() - start_time))


# newtonsFx(0.5, -5, 2, -3, 0.5)


c = 5
b = np.array([[-2], [1]])
A = np.array([[2, -1], [-1, 2]])
x = np.array([[10], [4]])

newtonsGx(A, b, c, x)
