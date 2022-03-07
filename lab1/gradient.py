import numpy as np
import time
from sympy import *


def gradientDescentFx(a, b, c, d, x):
    eps = 0.000001
    iterations = 5000
    learning_rate = 0.01

    x = Symbol('x')
    f = a*x**3+b*x**2+c*x+d
    f_prime = f.diff(x)
    f_prime = lambdify(x, f_prime)

    print("Starting computation of Gradient descent (Fx)")
    start_time = time.time()

    for i in range(iterations):
        x_new = x - learning_rate * f_prime(x)

        if (abs(x_new - x < eps) or (time.time() - start_time > 1)):
            break

        x = x_new

    print('Found x: ' + str(x))
    print('Nr of performed iterations: ' + str(i))
    print('Nr of seconds: ' + str((time.time() - start_time)))


def gradientDescentGx(A, b, c, x):
    eps = 0.00000000001
    iterations = 1000000
    learning_rate = 0.01

    print("Starting computation of Gradient descent (Gx)")
    start_time = time.time()

    for i in range(iterations):
        grad = np.add(np.dot(np.add(A, np.transpose(A)), x), b)

        x_new = x - np.multiply(grad, learning_rate)

        if ((x[0][0]-x_new[0][0] < eps and x[1][0]-x_new[1][0] < eps) or (time.time() - start_time) > 1):
            break

        x = x_new

    Gx = c + np.dot(np.transpose(b), x) + np.dot(np.dot(np.transpose(x), A), x)

    print('Found x: ' + str(x))
    print('G(x): ' + str(Gx))
    print('Nr of performed iterations: ' + str(i))
    print('Nr of seconds: ' + str((time.time() - start_time)))
