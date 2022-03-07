import numpy as np


def getStartPoint(func_type, d):
    start_point_type = 'scalar number' if func_type == 0 else 'initial vector'

    # chose starting point type
    start_method = int(input(
        'Chose how to define start point\n0 - ' + start_point_type + '\n1 - Generate from uniform distribution\nInput: '))

    while start_method not in [0, 1]:
        start_method = int(input('Insert 0 or 1! Input: '))

    if start_method == 0:  # inserted by user
        if func_type == 0:  # initial scalar number
            start_p = readScalar('starting point')
        else:  # initial vector
            start_p = np.zeros((d, 1))

            for i in range(d):
                start_p[i][0] = readScalar("x[{}]".format(i))
    else:  # generated from uniform distibution
        start_point_type = start_point_type.replace('initial ', '')

        low_rage = input('Insert low range ' + start_point_type + '\nInput: ')
        high_rage = input('Insert high range' + start_point_type + '\nInput: ')

        start_p = np.random.uniform(low_rage, high_rage)

    return start_p


def getPositiveDefineMatrix(matrix_dim):  # input positive define matrix A
    while True:
        matrix = np.zeros((matrix_dim, matrix_dim))
        for x in range(matrix_dim):
            for y in range(matrix_dim):
                matrix[x][y] = readScalar("A[{}][{}]".format(x, y))
        # check if matrix is positive-define
        if (not np.all(np.linalg.eigvals(matrix) > 0)):
            break
        print("Matrix, is not a positive definite matrix, please rewrite the data")

    return matrix


def getDimentionalVector(d):
    # d-dimensional vector full of 0s
    array = np.zeros((d, 1))

    # add 1s
    for i in range(d):
        array[i][0] = readScalar("b[{}][0]".format(i))

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
