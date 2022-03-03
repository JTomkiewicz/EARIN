import numpy as np


def gradient_descent(x, y):
    a_curr = b_curr = c_curr = d_curr = 0
    iterations = 10000
    n = float(len(x))
    learning_rate = 0.000001

    for i in range(iterations):
        y_predicted = a_curr * x**3 + b_curr * x**2 + c_curr * x + d_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        ad = -(2/n) * sum(x**3*(y-y_predicted))
        bd = -(2/n) * sum(x**2*(y-y_predicted))
        cd = -(2/n) * sum(x*(y-y_predicted))
        dd = -(2/n) * sum(y-y_predicted)
        a_curr = a_curr - learning_rate * ad
        b_curr = b_curr - learning_rate * bd
        c_curr = c_curr - learning_rate * cd
        d_curr = d_curr - learning_rate * dd
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
    return y


# x = np.array([-12, -2, 1, 12, 2, 4])
x = np.array([10, 1, 5, 3, 2])

y = expectedY(x, 0, 0, -3, 5)
print(x)
print(y)

gradient_descent(x, y)
