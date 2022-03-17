import random
import numpy as np


def fx(x, A, b, c):  # fx = x^T*A*x + b^T * x + c
    return (np.dot(np.dot(np.transpose(x), A), x) + np.dot(np.transpose(b), x) + c).item(0)


def fitness(x, A, b, c):
    ans = fx(x, A, b, c)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)


def geneticAlgorithm(A, b, c):
    solutions = np.array()

    for s in range(10000):
        solutions = np.append(
            solutions, [[random.uniform(-1000, 1000)],  [random.uniform(-1000, 1000)]])

    for i in range(10000):
        rankedsolutions = []

        for s in solutions:
            rankedsolutions.append((fitness(s, A, b, c), s))

        rankedsolutions.sort()
        rankedsolutions.reverse()

        print(f"=== Gen {i} best solutions ===")
        print(rankedsolutions[0])

        bestsolutions = rankedsolutions[:100]

        elements = []
        for s in bestsolutions:
            elements.append(s[1])

        new_gen = []
        print(elements[:10])

        for _ in range(10000):
            e1 = random.choice(elements)[0] * random.uniform(0.99, 1.01)
            e2 = random.choice(elements)[1] * random.uniform(0.99, 1.01)

            new_gen.append([[e1], [e2]])

        solutions = new_gen


# c = 5
# b = np.array([[-11], [1]])
# A = np.array([[21, -1], [-6, 2]])
# x = np.array([[10], [4]])

# print(fx(x, A, b, c).item(0))

# geneticAlgorithm(A, b, c)
