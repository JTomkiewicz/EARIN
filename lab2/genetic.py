import random
import numpy as np


def fx(x):  # f(x) = x^T*A*x + b^T*x + c
    return (np.dot(np.dot(np.transpose(x), A), x) + np.dot(np.transpose(b), x) + c).item(0)


def genomeString(g):  # convert genome to string
    return "".join(map(str, g))


def genomeInt(g):  # convert genome to int
    return int(genomeString(g), 2)


def createGenome(dim):  # create table that consist of two binary tables of length 10
    numberList = []
    for _ in range(dim):
        numberList.append(random.choices([0, 1], k=10))
    return numberList


# create population consisting of popSize genomes
def createPopulation(popSize, dim):
    return [createGenome(dim) for _ in range(popSize)]


def fitness(g):
    x = []
    for binaryList in g:
        x.append(genomeInt(binaryList))

    # check if values are out of range
    for number in x:
        if number >= 2**intRange or number < -2**intRange:
            return -1000

    # return result of func
    return fx(x)


def crossover(g1, g2):  # single point crossover
    # if different lengths quit
    if len(g1) != len(g2):
        print('genomes g1 and g2 are not the same length!')
        quit()

    # check if genomes have only 2 elements
    if len(g1) < 2:
        return g2, g1

    # random int where genomes will be cut
    ri = random.randint(1, len(g1) - 1)

    # cut genomes
    cross1 = g1[:ri] + g2[ri:]
    cross2 = g2[:ri] + g1[ri:]
    return [cross1, cross2]


def selection(population):
    # list of 2 randomly chosen elements of population
    return random.choices(population=population, weights=[fitness(g) for g in population], k=2)


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
        newGeneration = population[:2]

        for _ in range(int(len(population) / 2) - 1):
            # select best two genomes
            parents = selection(population)

            # perform crossover
            mutationList = []
            for j in range(dim):
                mutationList.append(crossover(parents[0][j], parents[1][j]))

            # mutation
            for j in range(dim):
                mutationList[j] = mutation(mutationList[j], mutatProb)

            # add new genome to generation
            newGeneration += mutationList

        population = newGeneration

        # sort population by best fitness desc
        population = sorted(
            population, key=lambda genome: fitness(genome), reverse=True)

    funcValue = fitness(population[0])
    # at the end print summary
    printSummary(i, population, funcValue, dim)
