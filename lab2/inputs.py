import numpy as np


def readScalar(msg: str):  # read input and check if it is a scalar number
    while True:
        try:
            number = input(f'Insert {msg}: ')
            number = float(number)
            break
        except ValueError:
            print('Input must be a scalar number!')

    return np.float64(number)


def readInt(msg: str):
    while True:
        try:
            number = input(f'Insert {msg}: ')
            number = int(number)
            break
        except ValueError:
            print('Input must be a int!')

    return int(number)


def getVector(dim: int):  # create and return vector b
    # array of zeros
    array = np.zeros((dim, 1))

    for i in range(dim):
        array[i][0] = readScalar('b[{}]'.format(i))

    return array


def getMatrix(dim: int):  # create and return matrix A
    # matrix of zeros
    matrix = np.zeros((dim, dim))

    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = readScalar('A[{}][{}]'.format(i, j))

    return np.matrix(matrix)


def getFunctionParams():  # create c, b and A
    # reac scalar number c
    c = readScalar('c')

    n = 0
    while n <= 0:  # n has to be > 0
        n = readInt('vector b length')

    # get matrix A and vector b
    b = getVector(n)
    A = getMatrix(n)

    return c, b, A


def getAlgorithmParams():
    popSize = readInt('population size')

    crossProb = readScalar('crossover probability')
    mutatProb = readScalar('mutation probability')

    n = readInt('number of algo iterations')

    return popSize, crossProb, mutatProb, n
