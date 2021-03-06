from bayesian import BayesianNetwork
from inputs import read_params


def main():
    # read program parameters
    evidence, query, nr_steps = read_params()

    # create & print a Bayesian network
    bn = BayesianNetwork("flu.json")
    bn.print_network()

    # run the Gibbs sampler & show results
    ret = bn.gibbs_sampler(evidence, query, nr_steps)
    for name, prediction in ret.items():
        print(name)
        print(
            f"True {prediction.get_result(True)}, False {prediction.get_result(False)}")


if __name__ == "__main__":
    main()
