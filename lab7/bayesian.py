from fileinput import filename
import json


class Node:
    def __init__(self, name, parents, probabilities):
        self.name = name
        self.parents = parents
        self.probabilities = probabilities


class BayesianNetwork:
    def __init__(self, file_name):
        self.nodes = []
        self.read_json(file_name)

    # read bayessian network from json file
    def read_json(self, file_name):
        with open(file_name, 'r') as f:
            network = json.load(f)

        # check if json file is valid
        if network.get('nodes') is None or network.get('relations') is None:
            raise Exception('Invalid json file!')

        # crete nodes
        for key in network['nodes']:
            node = Node(key, network['relations'][key]['parents'],
                        network['relations'][key]['probabilities'])
            self.nodes.append(node)

    # print bayesian network
    def print_network(self):
        print('\n--- Bayesian network: ---\n')
        for node in self.nodes:
            print(
                f'Name: {node.name}\nParents: {node.parents}\nProb: {node.probabilities}\n')
        print('--------------------------\n')

    # run MCM algorithm
    def mcm(self, evidence, query, nr_steps):
        pass
