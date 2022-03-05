from cmath import inf
import numpy as np
import math
import time
import threading
from sympy import *


def gradient_descent(x, y):
    a_curr = b_curr = c_curr = d_curr = 0
    iterations = 500000
    n = float(len(x))
    learning_rate = 0.000006
    cost_rising = 0
    cost = inf
    start_time = time.time()
    print("Starting computation of gradient descent")
    for i in range(iterations):
        # if (iterations%20000 == 0):
        #     print("current computation time = %s seconds (updated every 20k iterations)" % (time.time() - start_time), end = "\r")
        if (math.isnan(a_curr) or math.isnan(b_curr) or math.isnan(c_curr) or math.isnan(d_curr)):
            break
        y_predicted = a_curr * x**3 + b_curr * x**2 + c_curr * x + d_curr
        new_cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        if (new_cost > cost):
            cost_rising += 1
            if (cost_rising > 10):
                print("cost is rising isted of decresing, breaking the loop")
                break
        cost = new_cost
        # if (cost < 0.1):
        #     print("cost value low enough, breaking the loop")
        #     break
        ad = -(2/n) * sum(x**3*(y-y_predicted))
        bd = -(2/n) * sum(x**2*(y-y_predicted))
        cd = -(2/n) * sum(x*(y-y_predicted))
        dd = -(2/n) * sum(y-y_predicted)
        a_curr = a_curr - learning_rate * ad
        b_curr = b_curr - learning_rate * bd
        c_curr = c_curr - learning_rate * cd
        d_curr = d_curr - learning_rate * dd
    print("--- %s seconds ---" % (time.time() - start_time))
    print("a {}, b {}, c {}, d {}, cost {} iteration {}".format(
        a_curr, b_curr, c_curr, d_curr, cost, i))


def gradientDescent(a, b, c, d):
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


def gradientDescentG(A, b, c, x):
    eps = 0.000001
    iterations = 10000
    learning_rate = 0.01
    start_time = time.time()
    print("Starting computation of gradient descent")
    for i in range(iterations):
        grad = np.add(np.dot(np.add(A, np.transpose(A)), x), b)
        x = x - np.multiply(grad, learning_rate)
        if (time.time() - start_time > 1):
            break
    Gx = c + np.dot(np.transpose(b), x) + \
        np.dot(np.add(np.transpose(x), A), x)
    print(Gx)
    print(i)
    print("--- %s seconds ---" % (time.time() - start_time))


c = 5
b = np.array([[2], [1]])
A = np.array([[2, 5], [1, 3]])
x = np.array([[1], [0]])
print(np.add(np.dot(np.add(A, np.transpose(A)), x), b))
gradientDescentG(A, b, c, x)
# print(np.transpose(b))
# print(c + np.dot(np.transpose(b), x) +
#       np.dot(np.dot(np.transpose(x), A), x))

# gradientDescent(0.5, -5, 2, -3)
