from bayesian import BayesianNetwork
from inputs import read_params


def main():
    # read program parameters
    # evidence, query, nr_steps = read_params()
    # create a Bayesian network
    bn = BayesianNetwork('flu.json')
    # run the MCM algorithm
    # bn.mcm(evidence, query, nr_steps)


if __name__ == "__main__":
    main()
