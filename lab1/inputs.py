import numpy as np


def getStartPoint(func_type, d):  # generate or read start point
    start_point_type = 'scalar number' if func_type == 0 else 'initial vector'

    # starting point type
    print('Chose how to define start point\n0 - ' +
          start_point_type + '\n1 - Generate from uniform distribution')
    start_method = 2

    while start_method not in [0, 1]:
        start_method = readScalar('start method ID')
        if (start_method in [0, 1]):
            break
        print('Insert must be 0 or 1!')

    if start_method == 0:  # read from user
        if func_type == 0:  # initial scalar number
            start_p = readScalar('starting point')

        else:  # initial vector
            start_p = np.zeros((d, 1))

            for i in range(d):
                start_p[i][0] = readScalar('x[{}]'.format(i))

    else:  # generated from uniform distibution
        low_rage = readScalar('low range')
        high_rage = readScalar('high range')
        if func_type == 0:
            start_p = np.random.uniform(low_rage, high_rage)
        else:
            start_p = np.zeros((d, 1))

            for i in range(d):
                start_p[i][0] = np.random.uniform(low_rage, high_rage)

    return start_p


def getPositiveDefineMatrix(matrix_dim):  # create and return matrix A
    while True:
        matrix = np.zeros((matrix_dim, matrix_dim))

        for x in range(matrix_dim):
            for y in range(matrix_dim):
                matrix[x][y] = readScalar('A[{}][{}]'.format(x, y))

        # exit loop if matrix is positive-define
        if (np.all(np.linalg.eigvals(matrix) > 0)):
            break

        print('Matrix, is not a positive definite matrix!')

    return np.matrix(matrix)


def getDimentionalVector(d):  # create and return vector b
    array = np.zeros((d, 1))

    for i in range(d):
        array[i][0] = readScalar('b[{}]'.format(i))

    return array


def readScalar(letter):  # read input and check if it is a scalar number
    while True:
        try:
            number = input('Insert parameter ' + letter + '. Input: ')
            number = float(number)
            break
        except ValueError:
            print('Input must be a number!')
    return np.float64(number)


# for Fx read 4 scalars (abcd), for Gx read c scalar and ask for vector dimensions
def getParams(func_type):
    if(func_type == 0):  # Fx
        a = readScalar('a')
        b = readScalar('b')
        c = readScalar('c')
        d = readScalar('d')

        return a, b, c, d

    # Gx
    c = readScalar('c')

    vector_dim = int(input('Insert vector length. Input: '))

    while vector_dim <= 0:  # vector has to be bigger than 0
        vector_dim = int(input('Vector length must be > 0. Input: '))

    return c, vector_dim
