from cmath import inf
import numpy as np
import math
import time
import threading
from sympy import *


def newtons(a, b, c, d, start):
    x = Symbol('x')
    y = Symbol('y')
    f = a*x**3+b*x**2+c*x+d
    f_prime = f.diff(x)
    f_prime = lambdify(x, f_prime)

    f = lambdify(x, f)

    x_curr = start
    iterations = 0
    start_time = time.time()

    print("Starting computation of Newtons")
    # perform until value is bigger than eps
    while (abs(f(x_curr)) > 0.0001):
        # find new x
        x_curr = x_curr - f(x_curr)/f_prime(x_curr)
        # increate nr of performed iterations
        iterations += 1
        print(x_curr)

    print("--- %s seconds ---" % (time.time() - start_time))


newtons(0.5, -5, 2, -3, 0.5)
