import random
import numpy as np


def fx(x):  # f(x) = x^T*A*x + b^T*x + c
    return (np.dot(np.dot(np.transpose(x), A), x) + np.dot(np.transpose(b), x) + c).item(0)


def genomeInt(g):  # convert genome to int
    decimal = 0

    for index in range(len(g) - 1):
        decimal += g[index] * 2**index

    decimal -= g[-1] * 2**(len(g) - 1)
    return decimal


def createGenome(dim):  # create table that consist of two binary tables of length 10
    numberList = []
    for _ in range(dim):
        numberList.append(random.choices([0, 1], k=intRange+1))
    return numberList


# create population consisting of popSize genomes
def createPopulation(popSize, dim):
    return [createGenome(dim) for _ in range(popSize)]


def fitness(g):
    x = []
    for binaryList in g:
        x.append(genomeInt(binaryList))
    # return result of func
    return fx(x)


def crossover(g1, g2, prob):  # single point crossover
    # if different lengths quit
    if len(g1) != len(g2):
        print('genomes g1 and g2 are not the same length!')
        quit()

    if random.random() > prob:
        return g1, g2

    # check if genomes have only 2 elements
    if len(g1) < 2:
        return g2, g1

    # random int where genomes will be cut
    ri = random.randint(1, len(g1) - 1)

    # cut genomes
    cross1 = g1[:ri] + g2[ri:]
    cross2 = g2[:ri] + g1[ri:]
    return [cross1, cross2]


def selection(population):  # list of 2 randomly chosen elements of population
    functionValues = []
    valuesSum = 0
    currentMin = fitness(population[0])

    for genome in population:
        val = fitness(genome)

        if val < currentMin:
            currentMin = val

        functionValues.append(val)
        valuesSum += val

    weightsList = []

    for value in functionValues:
        weightsList.append(value-currentMin)

    return random.choices(population=population, weights=weightsList, k=2)


def mutation(g, prob):
    ri = random.randrange(len(g))
    # change random values
    g[ri] = g[ri] if random.random() > prob else abs(g[ri] - 1)
    return g


def printSummary(i, population, funcValue, dim):
    print(f'Nr of iterations: {i}')

    for index in range(dim):
        print(f'x{index}: {genomeInt(population[0][index])}')

    print(f'f(x): {funcValue}')


def geneticAlgorithm(popSize, crossProb, mutatProb, n, _A, _b, _c, _intRange, dim):
    # set global variables
    global A, b, c, intRange
    A, b, c, intRange = _A, _b, _c, _intRange

    # generate new population
    population = createPopulation(popSize, dim)

    # go throught n number of iterations
    for i in range(n):
        # sort population by best fitness desc
        population = sorted(
            population, key=lambda g: fitness(g), reverse=True)

        # take two best genomes
        newPopulation = population[:2]

        for _ in range(int(len(population) / 2) - 1):
            # select best two genomes
            parents = selection(population)

            # crossover
            crossoverList = []

            for j in range(dim):
                crossoverList.append(
                    crossover(parents[0][j], parents[1][j], crossProb))

            # mutation
            for j in crossoverList:
                for k in j:
                    k = mutation(k, mutatProb)

            firstGenome = []
            secondGenome = []
            for index in range(dim):
                firstGenome.append(crossoverList[index][0])
                secondGenome.append(crossoverList[index][1])

            # add new genome to generation
            newPopulation += firstGenome
            newPopulation += secondGenome

        population = newPopulation

        # sort population by best fitness desc
        population = sorted(
            population, key=lambda genome: fitness(genome), reverse=True)

    funcValue = fitness(population[0])
    # at the end print summary
    printSummary(i, population, funcValue, dim)
