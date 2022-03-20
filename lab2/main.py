# inputs validator
import inputs
# genetic algorithm
import genetic


def main():
    # get problem dimensionality
    dim = inputs.getRange('problem dimensionality')

    # get c, b, A params
    c, b, A = inputs.getFunctionParams(dim)

    # get range of serched integers
    d = inputs.getRange('d')

    # get algo params
    popSize, crossProb, mutatProb, n = inputs.getAlgorithmParams()

    # perform algo
    genetic.geneticAlgorithm(popSize, crossProb, mutatProb, n, A, b, c, d, dim)


if __name__ == "__main__":
    main()

# c = 5
# b = np.array([[-11], [1]])
# A = np.array([[21, -1], [-6, 2]])

# geneticAlgorithm(10, 0.5, 0.5, 10000, A, b, c)
