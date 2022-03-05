def f0(x):
    return 3*x**2 - 6*x - 45


def f1(x):
    return 6*x - 6


def newtons(func, dfunc, start, eps=0.0001):
    count = 0  # counter for nr of performed iterations
    x = start  # start point

    # func value at 1st given start point
    f = func(x)

    # perform until value is bigger than eps
    while (abs(f) > eps):
        # f(x) and df(x) at x
        f = func(x)
        df = dfunc(x)

        # find new x
        x = x - (f)/(df)

        # increate counter
        count += 1

    print(f"{count} iterations performed\nOptimal point is {x}")


newtons(f0, f1, 50)
