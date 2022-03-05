import numpy as np


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
