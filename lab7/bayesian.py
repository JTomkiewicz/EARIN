from fileinput import filename
import json
import random
from numpy.random import choice


class Node:
    def __init__(self, name, parents, probabilities):
        self.name = name
        self.parents = parents
        self.probabilities = probabilities

    def get_probability(self, first_condition, second_condition=None):
        if second_condition == None:
            if first_condition == True:
                return self.probabilities["T"]
            return self.probabilities["F"]
        if first_condition == True:
            if second_condition == True:
                return self.probabilities["T,T"]
            return self.probabilities["T,F"]
        if second_condition == True:
            return self.probabilities["F,T"]
        return self.probabilities["F,F"]


class ProbabilityStructure:
    def __init__(self):
        self.total = 0
        self.total_true = 0
        self.total_false = 0

    def add_count(self, condition):
        if condition == True:
            self.total_true += 1
        else:
            self.total_false += 1
        self.total += 1

    def get_result(self, condition):
        if condition == True:
            return self.total_true / self.total
        return self.total_false / self.total


class BayesianNetwork:
    def __init__(self, file_name):
        self.nodes = {}
        self.read_json(file_name)

    def read_json(self, file_name):
        with open(file_name, "r") as f:
            network = json.load(f)

        # check if json file is valid
        if network.get("nodes") is None or network.get("relations") is None:
            raise Exception("Invalid json file!")

        # crete nodes
        for key in network["nodes"]:
            node = Node(
                key,
                network["relations"][key]["parents"],
                network["relations"][key]["probabilities"],
            )
            self.nodes[node.name] = node

    # print bayesian network
    def print_network(self):
        print("\n--- Bayesian network: ---\n")
        for node in self.nodes.values():
            print(
                f"Name: {node.name}\nParents: {node.parents}\nProb: {node.probabilities}\n"
            )
        print("-------------------------\n")

    # run gibbs algorithm
    def gibbs_sampler(self, selected_variables, query, nr_steps):
        variables = selected_variables
        variables_to_predict = [
            name for name in self.nodes if name not in selected_variables
        ]

        # set random values for not selected variables
        for name in variables_to_predict:
            variables[name] = random.choice([False, True])

        # create empty probability structures
        query_predictions = {}
        for name in query:
            query_predictions[name] = ProbabilityStructure()

        # random walk (gibbs sampling)
        for _ in range(nr_steps):
            current_choice = random.choice(variables_to_predict)
            predicted_choice = self.give_prediction(
                variables, current_choice)
            variables[current_choice] = predicted_choice
            query_predictions[current_choice].add_count(predicted_choice)

        return query_predictions

    def give_prediction(self, variables, current_choice):
        probabilities = []

        chosen_node = self.nodes[current_choice]

        # HighFever (has parents)
        if len(chosen_node.parents) > 0:
            for condition in ([True, False]):
                probabilities.append(
                    chosen_node.get_probability(variables["Flu"], condition))
        else:  # Flu (has no parents)
            for condition in ([True, False]):
                probability = chosen_node.get_probability(
                    condition)
                probability *= self.nodes["HighFever"].get_probability(
                    condition, variables["Flu"])
                probabilities.append(probability)
            # scaling of probabilities
            probabilities = [p / sum(probabilities) for p in probabilities]

        return choice([True, False], p=probabilities)
