from cmath import inf
import numpy as np
import math
import time
import threading


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
        if (cost < 0.1):
            print("cost value low enough, breaking the loop")
            break
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

# y = ax^3 + bx^2 + cx + d
# 1st a b c d
# 2nd startX = 10
# 2nd [0, 10]
# uniform distribution, in statistics, distribution function in which every possible result is equally likely; that is, the probability of each occurring is the same


def expectedY(x_array, a, b, c, d):
    y = []
    for x in x_array:
        y.append(a*x**3 + b*x**2 + c*x + d)
    return np.array(y)

x = np.array([-2, 1.8, 1.6, 1,4, 1, -0.7, -0.2, -0, 0.5, -1, -1.5, 2, 2.5, 3, 10, -10, -0.4 ])

y = expectedY(x, 0.1, -1, -3, 11)
gradient_descent(x, y)
