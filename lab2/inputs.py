import numpy as np


def readScalar(msg: str):  # read input and check if it is scalar
    while True:
        try:
            number = input(f'Insert {msg}: ')
            number = float(number)
            break
        except ValueError:
            print('Input must be a scalar number!')

    return np.float64(number)


def readInt(msg: str):  # read input and check if it is integer
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


def getFunctionParams(dim: int):  # read c, b, A
    # reac scalar number c
    c = readScalar('c')

    # get matrix A and vector b
    b = getVector(dim)
    A = getMatrix(dim)

    return c, b, A


def getAlgorithmParams():  # read algo params
    popSize = readInt('population size')

    crossProb = readScalar('crossover probability')
    mutatProb = readScalar('mutation probability')

    n = readInt('number of algo iterations')

    return popSize, crossProb, mutatProb, n


def getRange(msg: str):
    d = readInt(msg)
    while d < 1:
        d = readInt(msg)
    return d
