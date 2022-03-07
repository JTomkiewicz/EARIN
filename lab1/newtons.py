import numpy as np
import time


def newtonsFx(a, b, c, d, x):
    eps = 0.000001
    iterations = 5000

    def f(x):
        return a*x**3 + b*x**2 + c*x + d

    def f_prime(x):
        return 3*a*x**2 + 2*b*x + c

    def f_prime2(x):
        return 6*a*x + 2*b

    print("Starting computation of Newtons (Fx)")
    start_time = time.time()

    for i in range(iterations):
        x_new = x - f_prime(x)/f_prime2(x)

        if (abs(x - x_new) < eps or time.time() - start_time > 1):
            break

        x = x_new

    print('Found x: ' + str(x))
    print('F(x): ' + str(f(x)))
    print('Nr of performed iterations: ' + str(i))
    print('Nr of seconds: ' + str((time.time() - start_time)))


def newtonsGx(A, b, c, x):
    eps = 0.00000000001
    iterations = 1000000
    learning_rate = 0.01

    print("Starting computation of Newtons (Gx)")
    start_time = time.time()

    for i in range(iterations):
        f_prime = np.add(np.dot(np.add(A, np.transpose(A)), x), b)

        f_prime2 = np.add(np.transpose(A), A)

        x_new = x - np.dot(np.dot(np.linalg.inv(f_prime2),
                           f_prime), learning_rate)

        if ((x[0][0]-x_new[0][0] < eps and x[1][0]-x_new[1][0] < eps) or (time.time() - start_time > 1)):
            break

        x = x_new

    Gx = c + np.dot(np.transpose(b), x) + np.dot(np.dot(np.transpose(x), A), x)

    print('Found x: ' + str(x))
    print('G(x): ' + str(Gx))
    print('Nr of performed iterations: ' + str(i))
    print('Nr of seconds: ' + str((time.time() - start_time)))
