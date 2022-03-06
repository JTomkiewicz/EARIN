from cmath import inf
import numpy as np
import math
import time
import threading
from sympy import *


def newtonsFx(a, b, c, d, x):
    eps = 0.000001
    iterations = 5000

    def f(x):
        return a*x**3 + b*x**2 + c*x + d

    def f_prime(x):
        return 3*a*x**2 + 2*b*x + c

    def f_prime2(x):
        return 6*a*x + 2*b

    start_time = time.time()

    print("Starting computation of Newtons")

    for i in range(iterations):
        x_new = x - f_prime(x)/f_prime2(x)
        if (abs(x - x_new) < eps or time.time() - start_time > 1):
            break
        x = x_new
    print(x)
    print(i)
    print("--- %s seconds ---" % (time.time() - start_time))


def newtonsGx(A, b, c, x):
    eps = 0.00000000001
    iterations = 1000000
    learning_rate = 0.01

    start_time = time.time()

    print("Starting computation of Newtons")
    for i in range(iterations):
        f_prime = np.add(np.dot(np.add(A, np.transpose(A)), x), b)

        f_prime2 = np.add(np.transpose(A), A)

        x_new = x - np.multiply(np.divide(f_prime, f_prime2), learning_rate)

        if ((x[0][0]-x_new[0][0] < eps and x[1][0]-x_new[1][0] < eps and x[0][1]-x_new[0][1] < eps and x[1][1]-x_new[1][1] < eps) or (time.time() - start_time > 1)):
            print('breaking')
            break

        x = x_new

    print(x)
    print(i)
    print("--- %s seconds ---" % (time.time() - start_time))


# newtonsFx(0.5, -5, 2, -3, 0.5)


c = 5
b = np.array([[-2], [1]])
A = np.array([[2, -1], [-1, 2]])
x = np.array([[10], [4]])

newtonsGx(A, b, c, x)
