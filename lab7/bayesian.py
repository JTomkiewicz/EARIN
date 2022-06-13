class BayesianNetwork:
    def __init__(self, filename):
        self.nodes = []
        self.edges = []
        self.read_json(filename)

    def read_json(self, filename):
        pass
