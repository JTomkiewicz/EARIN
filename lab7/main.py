from bayesian import BayesianNetwork
from inputs import read_params


def main():
    # read program parameters
    # evidence, query, nr_steps = read_params()
    # create and print a Bayesian network
    bn = BayesianNetwork("flu.json")
    bn.print_network()
    # run the MCM algorithm
    evidence = {"Flu": True}
    query = ["HighFever"]
    nr_steps = 1000
    ret = bn.gibbs_sampler(evidence, query, nr_steps)
    for name, prediction in ret.items():
        print(name)
        print(
            f"True {prediction.get_result(True)}, False {prediction.get_result(False)}")


if __name__ == "__main__":
    main()
