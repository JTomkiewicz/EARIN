import numpy as np


# def gradient_descent(x, y):
#     m_curr = b_curr = 0
#     iterations = 10000
#     n = len(x)
#     learning_rate = 0.08

#     for i in range(iterations):
#         y_predicted = m_curr * x + b_curr
#         cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
#         ad = -(2/n) * sum(x**3*(y-y_predicted))
#         bd = -(2/n) * sum(x**2*(y-y_predicted))
#         cd = -(2/n) * sum(x*(y-y_predicted))
#         dd = -(2/n) * sum(y-y_predicted)
#         a_curr = a_curr - learning_rate * ad
#         b_curr = b_curr - learning_rate * bd
#         c_curr = c_curr - learning_rate * cd
#         d_curr = d_curr - learning_rate * dd
#         print("a {}, b {}, c {}, d {}, cost {} iteration {}".format(
#             a_curr, b_curr, c_curr, d_curr, cost, i))

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 7, 9, 11, 13])

# gradient_descent(x, y)

def getStartPoint(func_type):
    start_point_type = 'scalar number' if func_type == 0 else 'initial vector'

    # chose starting point type
    start_method = int(input(
        'Chose how to define start point\n0 - ' + start_point_type + '\n1 - Generate from uniform distribution\nInput: '))

    while start_method not in [0, 1]:
        start_method = int(input('Insert 0 or 1! Input: '))

    if start_method == 0:  # inserted by user
        if func_type == 0:  # scalar number
            start_p = input('Insert starting point\nInput: ')

            while not np.isscalar(start_p):  # point must be scalar
                start_p = input('Nr must be scalar! Input: ')
        else:  # initial vector
            print('')
    else:  # generated from uniform distibution
        start_point_type = start_point_type.replace('initial ', '')

        low_rage = input('Insert low range ' + start_point_type + '\nInput: ')
        high_rage = input('Insert high range' + start_point_type + '\nInput: ')

        start_p = np.random.uniform(low_rage, high_rage)

    return start_p


def getPositiveDefineMatrix():  # input positive define matrix A
    params = input(
        'Give params for matrix A. Rows have to be separated by ;\nInput: ')
    # use numpy to create matrix
    matrix = np.matrix(params)

    # check if matrix is positive-define
    if not np.all(np.linalg.eigvals(matrix) > 0):
        params = input('Matrix must be positive-define! Input: ')
        matrix = np.matrix(params)

    return matrix


def getDimentionalVector(d):
    # d-dimensional vector full of 0s
    array = np.zeros((d, d))

    # add 1s
    for x in range(1, d):
        array[x-1][x] = 1

    return array


def getParams(func_type):
    # empty dictionary
    p = dict()

    # func F(x)
    if(func_type == 0):
        for letter in ['a', 'b', 'c', 'd']:
            p[letter] = input('Insert parameter ' + letter + '\nInput: ')

            while not np.isscalar(p[letter]):  # abcd must be scalar nrs
                p[letter] = input('Nr must be scalar! Input: ')
    else:  # func G(x)
        p['c'] = input('Insert parameter c\nInput: ')

        while not np.isscalar(p['c']):  # c must be scalar nr
            p['c'] = input('Nr must be scalar! Input: ')

        p['vectorDimension'] = int(input('Insert vector d dimension\nInput: '))

        while not p['vectorDimension'] > 0:
            p['vectorDimension'] = int(
                input('Vector dimension must be > 0\nInput: '))

    # return dictionary
    return p


def main():
    # chose method
    chosen_method = int(input(
        'Chose function minimalisation method\n0 - Gradient Descent\n1 - Newtons\nInput: '))

    while chosen_method not in [0, 1]:
        chosen_method = int(input('Insert 0 or 1! Input: '))

    # chose type of func
    chosen_func_type = int(input(
        'Chose function type\n0 - F(x) = ax^3 + bx^2 + cx + d\n1 - G(x) = c + b^Tx + x^TAx\nInput: '))

    while chosen_func_type not in [0, 1]:
        chosen_func_type = int(input('Insert 0 or 1! Input: '))

    # get scalar parameters
    params = getParams(chosen_func_type)

    # when G(x) then create vector b and matrix A
    if(chosen_func_type == 1):
        params['b'] = getDimentionalVector(params['vectorDimension'])
        params['A'] = getPositiveDefineMatrix()

    starting_point = getStartPoint(chosen_func_type)


if __name__ == "__main__":
    main()
