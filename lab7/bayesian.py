from fileinput import filename
import json


class BayesianNetwork:
    def __init__(self, file_name):
        self.src_file = file_name
        self.nodes = []
        self.edges = []
        self.read_json()

    def read_json(self):
        with open(self.src_file, 'r') as f:
            network = json.load(f)

        print(network)

    def mcm(self, evidence, query, nr_steps):
        pass
