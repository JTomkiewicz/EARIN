import random
import numpy as np


def fx(x, A, b, c):  # f(x) = x^T*A*x + b^T*x + c
    return (np.dot(np.dot(np.transpose(x), A), x) + np.dot(np.transpose(b), x) + c).item(0)


def genomeString(g):  # convert genome to string
    return "".join(map(str, g))


def genomeInt(g):  # convert genome to int
    return int(genomeString(g), 2)


def createGenome():  # create table that consist of two binary tables of length 10
    num1 = random.choices([0, 1], k=10)
    num2 = random.choices([0, 1], k=10)
    return [num1, num2]


def createPopulation(popSize):  # create population consisting of popSize genomes
    return [createGenome() for _ in range(popSize)]


def fitness(g1, g2, A, b, c, d):
    num1 = genomeInt(g1)
    num2 = genomeInt(g2)

    # check if values are out of range
    if num1 >= 2**d or num2 >= 2**d or num1 < -2**d or num2 < -2**d:
        return -1000

    # create vector that will be passed to func
    x = [num1, num2]
    # return result of func
    return fx(x, A, b, c)


def crossover(g1, g2):  # single point crossover
    # if different lengths quit
    if len(g1) != len(g2):
        print('genomes g1 and g2 are not the same length!')
        quit()

    # check if genomes have only 2 elements
    if len(g1) < 2:
        return g1, g2

    # random int where genomes will be cut
    ri = random.randint(1, len(g1) - 1)

    # cut genomes
    cross1 = g1[:ri] + g2[ri:]
    cross2 = g2[:ri] + g1[ri:]
    return [cross1, cross2]


def selection(population, A, b, c, d):
    # list of 2 randomly chosen elements of population
    return random.choices(population=population, weights=[fitness(g[0], g[1], A, b, c, d) for g in population], k=2)


def mutation(g, prob):
    ri = random.randrange(len(g))
    # change random values
    g[ri] = g[ri] if random.random() > prob else abs(g[ri] - 1)
    return g


def printSummary(i, population, funcValue):
    print(f'Nr of iterations: {i}')
    print(f'x0: {genomeInt(population[0][0])}')
    print(f'x1: {genomeInt(population[0][1])}')
    print(f'f(x): {funcValue}')


def geneticAlgorithm(popSize, crossProb, mutatProb, n, A, b, c, d):
    # generate new population
    population = createPopulation(popSize)

    # go throught n number of iterations
    for i in range(n):
        # sort population by best fitness desc
        population = sorted(
            population, key=lambda genome: fitness(genome[0], genome[1], A, b, c, d), reverse=True)

        # take two best genomes
        newGeneration = population[:2]

        for _ in range(int(len(population) / 2) - 1):
            # select two genomes
            parents = selection(population, A, b, c, d)

            # perform crossover
            firstCrossover = crossover(parents[0][0], parents[1][0])
            secondCrossover = crossover(parents[0][1], parents[1][1])

            # perform mutation for x0
            firstMutation = mutation(firstCrossover[0], mutatProb)
            secondMutation = mutation(firstCrossover[1], mutatProb)

            # perform mutation for x1
            thirdMutation = mutation(secondCrossover[0], mutatProb)
            forthMutation = mutation(secondCrossover[1], mutatProb)

            # add new genome to generation
            newGeneration += [[firstMutation, secondMutation],
                              [thirdMutation, forthMutation]]

        population = newGeneration

        # sort population by best fitness desc
        population = sorted(
            population, key=lambda genome: fitness(genome[0], genome[1], A, b, c, d), reverse=True)

    funcValue = fitness(population[0][0], population[0][1], A, b, c, d)
    # at the end print summary
    printSummary(i, population, funcValue)
