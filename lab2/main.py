# inputs validator
import inputs

# genetic algorithm
import genetic


def main():
    c, b, A = inputs.getFunctionParams()

    d = inputs.readInt('d')

    popSize, crossProb, mutatProb, n = inputs.getAlgorithmParams()

    genetic.geneticAlgorithm(popSize, crossProb, mutatProb, n, A, b, c, d)


if __name__ == "__main__":
    main()

# c = 5
# b = np.array([[-11], [1]])
# A = np.array([[21, -1], [-6, 2]])

# geneticAlgorithm(10, 0.5, 0.5, 10000, A, b, c)
