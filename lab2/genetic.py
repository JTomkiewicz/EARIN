import random
import numpy as np


def fx(x, A, b, c):
    return (np.dot(np.dot(np.transpose(x), A), x) + np.dot(np.transpose(b), x) + c).item(0)


def fitness(g1, g2, A, b, c):
    num1 = int(genomeString(g1), 2)
    num2 = int(genomeString(g2), 2)

    if num1 > 1000 or num2 > 1000 or num1 < -1000 or num2 < -1000:
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

    return g1[:ri] + g2[ri:], g2[:ri] + g1[ri:]


def selection(pop):
    # list of 2 randomly chosen elements of population
    return random.choices(population=pop, weights=[fitness(g) for g in pop], k=2)


def mutation(g, n=1, probability=0.5):
    for _ in range(n):
        # random index
        i = random.randrange(len(g))
        # change random values
        g[i] = g[i] if random() > probability else str(abs(int(g[i]) - 1))

    return g


def createGenome():
    num1 = random.choices([0, 1], k=10)
    num2 = random.choices([0, 1], k=10)
    return [num1, num2]


def createPopulation(popSize):
    return [createGenome() for _ in range(popSize)]


def genomeString(g):
    return "".join(map(str, g))


def geneticAlgorithm(populationSize, crossoverProb, mutationProb, nrOfIterations, A, b, c):
    population = createPopulation(populationSize)

    for i in range(nrOfIterations):
        population = sorted(
            population, key=lambda genome: fitness(genome[0], genome[1], A, b, c), reverse=True)

        newGeneration = population[:2]

        print(newGeneration)
    return


c = 5
b = np.array([[-11], [1]])
A = np.array([[21, -1], [-6, 2]])
# x = np.array([[10], [4]])

# print(fx(x, A, b, c).item(0))

geneticAlgorithm(3, 0.5, 0.5, 5, A, b, c)
