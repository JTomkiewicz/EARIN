import numpy as np


def readScalar(msg):  # read input and check if it is a scalar number
    while True:
        try:
            number = input('Insert ' + msg + ': ')
            number = float(number)
            break
        except ValueError:
            print('Input must be a number!')

    return np.float64(number)


def getVector(dimensions):  # create and return vector b
    # array of zeros
    array = np.zeros((dimensions, 1))

    for i in range(dimensions):
        array[i][0] = readScalar('b[{}]'.format(i))

    return array


def getMatrix(dimensions):  # create and return matrix A
    # matrix of zeros
    matrix = np.zeros((dimensions, dimensions))

    for i in range(dimensions):
        for j in range(dimensions):
            matrix[i][j] = readScalar('A[{}][{}]'.format(i, j))

    return np.matrix(matrix)


def getParams():  # create c, b and A
    # reac scalar number c
    c = readScalar('c')

    n = int(input('Insert n: '))

    while n <= 0:  # n has to be > 0
        n = int(input('n length must be > 0. Input: '))

    # get matrix A and vector b
    b = getVector(n)
    A = getMatrix(n)

    return c, b, A
