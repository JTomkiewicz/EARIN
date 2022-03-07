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
            start_p = readScalar('starting point')
        else:  # initial vector
            print('')
    else:  # generated from uniform distibution
        start_point_type = start_point_type.replace('initial ', '')

        low_rage = input('Insert low range ' + start_point_type + '\nInput: ')
        high_rage = input('Insert high range' + start_point_type + '\nInput: ')

        start_p = np.random.uniform(low_rage, high_rage)

    return start_p


def getPositiveDefineMatrix(matrix_dim):  # input positive define matrix A
    params = input(
        'Give params for matrix A. Rows have to be separated by ; (example: 2 -1; -1 2)\nInput: ')
    # use numpy to create matrix
    matrix = np.matrix(params)

    dimentions = str(matrix_dim) + 'x' + str(matrix_dim)

    # check if matrix is positive-define and has matrix_dim nr of rows
    while np.all(np.linalg.eigvals(matrix) <= 0 or matrix.shape[0] == matrix_dim):
        params = input(
            'Matrix must be positive-define and their dimensions have to be ' + dimentions + '! Input: ')
        matrix = np.matrix(params)

    return matrix


def getDimentionalVector(d):
    # d-dimensional vector full of 0s
    array = np.zeros((d, d))

    # add 1s
    for x in range(1, d):
        array[x-1][x] = 1

    return array


def readScalar(letter):
    while True:
        try:
            number = input('Insert parameter ' + letter + '\nInput: ')
            number = float(number)
            break
        except ValueError:
            print("Input must be a number!")
    return float(number)


def getParams(func_type):
    if(func_type == 0):  # Fx
        a = readScalar('a')
        b = readScalar('b')
        c = readScalar('c')
        d = readScalar('d')

        return a, b, c, d

    # Gx
    c = readScalar('c')

    vector_dim = int(input('Insert vector d dimension\nInput: '))

    while not vector_dim > 0:  # vector has to be bigger than 0
        vector_dim = int(input('Vector dimension must be > 0\nInput: '))

    return c, vector_dim
