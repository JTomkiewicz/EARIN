import numpy as np


def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
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


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)


def getPositiveDefineMatrix():  # input positive define matrix A
    params = input(
        'Give params for matrix A. Rows have to be separated by ;\nInput: ')
    matrix = np.matrix(params)
    if not np.all(np.linalg.eigvals(matrix) > 0):
        print('Matrix is not positive define')
        quit()
    return matrix


def getDimentionalVector(d):  # input d-dimensional vector
    array = np.zeros((d, d))
    for x in range(1, d):
        array[x-1][x] = 1
    return array


def getParams(funcType):
    p = dict()

    if(funcType == 0):
        a, b, c, d = input('Insert parameters: a b c d\nInput: ').split()
        p['a'] = a
        p['b'] = b
        p['c'] = c
        p['d'] = d
        return p
    else:
        p['c'] = input('Insert parameter c\nInput: ')
        p['vectorDimension'] = int(input('Insert vector d dimension\nInput: '))
        return p


def main():
    # chose method
    chosen_method = int(input(
        'Welcome!\nChose function minimalisation method:\n0 - Gradient Descent\n1 - Newtons\nInput: '))

    if(chosen_method not in [0, 1]):
        print('Incorrect method!')
        quit()

    # chose type of func
    chosen_func_type = int(input(
        'Chose function type:\n0 - F(x) = ax^3 + bx^2 + cx + d\n1 - G(x) = c + b^Tx + x^TAx\nInput: '))

    if(chosen_func_type not in [0, 1]):
        print('Incorrect function type!')
        quit()

    # get scalar parameters
    params = getParams(chosen_func_type)

    # when G(x), then create vector b and matrix A
    if(chosen_func_type == 1):
        params['b'] = getDimentionalVector(params['vectorDimension'])
        params['A'] = getPositiveDefineMatrix()


if __name__ == "__main__":
    main()
