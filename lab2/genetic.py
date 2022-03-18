import random
import numpy as np


def fx(x, A, b, c):
    return (np.dot(np.dot(np.transpose(x), A), x) + np.dot(np.transpose(b), x) + c).item(0)


def fitness(g1, g2, A, b, c, d):
    num1 = int(genomeString(g1), 2)
    num2 = int(genomeString(g2), 2)

    if num1 >= 2**d or num2 >= 2**d or num1 < -2**d or num2 < -2**d:
        return -1000

    x = [num1, num2]
    # get result of func for given params
    return fx(x, A, b, c)


def crossover(g1, g2):  # single point crossover
    # if different lengths quit
    if len(g1) != len(g2):
        print('genomes g1 and g2 are not the same length!')
        quit()

    if len(g1) < 2:
        return g1, g2

    # random int where genomes will be cut
    ri = random.randint(1, len(g1) - 1)

    cross1 = g1[:ri] + g2[ri:]
    cross2 = g2[:ri] + g1[ri:]

    return [cross1, cross2]


def selection(population, A, b, c, d):
    # list of 2 randomly chosen elements of population
    return random.choices(population=population, weights=[fitness(g[0], g[1], A, b, c, d) for g in population], k=2)


def mutation(g, probability):
    i = random.randrange(len(g))
    # change random values
    g[i] = g[i] if random.random() > probability else abs(g[i] - 1)

    return g


def createGenome():
    num1 = random.choices([0, 1], k=10)
    num2 = random.choices([0, 1], k=10)
    return [num1, num2]


def createPopulation(popSize):
    return [createGenome() for _ in range(popSize)]


def genomeString(g):
    return "".join(map(str, g))


def geneticAlgorithm(popSize, crossProb, mutatProb, n, A, b, c, d):
    population = createPopulation(popSize)

    for i in range(n):
        population = sorted(
            population, key=lambda genome: fitness(genome[0], genome[1], A, b, c, d), reverse=True)

        newGeneration = population[:2]

        for _ in range(int(len(population) / 2) - 1):
            parents = selection(population, A, b, c, d)

            firstCrossover = crossover(parents[0][0], parents[1][0])
            secondCrossover = crossover(parents[0][1], parents[1][1])

            firstMutation = mutation(firstCrossover[0], mutatProb)
            secondMutation = mutation(firstCrossover[1], mutatProb)

            thirdMutation = mutation(secondCrossover[0], mutatProb)
            forthMutation = mutation(secondCrossover[1], mutatProb)

            newGeneration += [[firstMutation, secondMutation],
                              [thirdMutation, forthMutation]]

        population = newGeneration

        population = sorted(
            population, key=lambda genome: fitness(genome[0], genome[1], A, b, c, d), reverse=True)

        # print(f'iteration: {i}')
        # print(f'f(x): {fitness(population[0][0], population[0][1], A, b, c)}')

    print(f'Nr of iterations: {i}')
    print(f'x0: {int(genomeString(population[0][0]), 2)}')
    print(f'x1: {int(genomeString(population[0][1]), 2)}')
    print(f'f(x): {fitness(population[0][0], population[0][1], A, b, c, d)}')
