from bayesian import BayesianNetwork
from inputs import read_params


def main():
    # read program parameters
    evidence, query, nr_steps = read_params()
    # create and print a Bayesian network
    bn = BayesianNetwork('flu.json')
    bn.print_network()
    # run the MCM algorithm
    bn.gibbs_sampler(evidence, query, nr_steps)


if __name__ == "__main__":
    main()
