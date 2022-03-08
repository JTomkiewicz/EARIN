import numpy as np
import time


def gradientDescentFx(a, b, c, d, x):
    eps = 10**-10
    iterations = 5000
    learning_rate = 0.01

    def f(x):
        return a*x**3 + b*x**2 + c*x + d

    def f_prime(x):
        return 3*a*x**2 + 2*b*x + c

    print("Starting computation of Gradient descent (Fx)")
    start_time = time.time()

    for i in range(iterations):
        x_new = x - learning_rate * f_prime(x)

        if (abs(x_new - x) <= eps or (time.time() - start_time > 1)):
            break

        if(abs(x_new - x) > 1e100):
            print(
                'Breaking! Your function is probably going to minus inf. Check params!')
            return 0, 0

        x = x_new

    print('Nr of performed iterations: ' + str(i))
    print('Nr of seconds: ' + str((time.time() - start_time)))

    return x, f(x)


def gradientDescentGx(A, b, c, x):
    eps = 10**-10
    iterations = 1000000
    learning_rate = 0.01

    print("Starting computation of Gradient descent (Gx)")
    start_time = time.time()

    for i in range(iterations):
        grad = np.add(np.dot(np.add(A, np.transpose(A)), x), b)

        x_new = x - np.multiply(grad, learning_rate)

        if ((x[0][0]-x_new[0][0] < eps and x[1][0]-x_new[1][0] < eps) or (time.time() - start_time) > 1):
            break

        if(abs(x_new[0][0] - x[0][0]) > 1e100 and abs(x_new[1][0] - x[1][0]) > 1e100):
            print(
                'Breaking! Your function is probably going to minus inf. Check params!')
            return 0, 0

        x = x_new

    Gx = c + np.dot(np.transpose(b), x) + np.dot(np.dot(np.transpose(x), A), x)

    print('Nr of performed iterations: ' + str(i))
    print('Nr of seconds: ' + str((time.time() - start_time)))

    return x, Gx.item(0)

# left for test purposes
# c = 5
# b = np.array([[-11], [1]])
# A = np.array([[21, -1], [-6, 2]])
# x = np.array([[10], [4]])

# gradientDescentGx(A, b, c, x)
