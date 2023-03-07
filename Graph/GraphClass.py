

class GraphClass:
    def __init__(self):
        self.edges = {}
        self.nodes = {}
        self.degree = {}
        self.zones = {}

    def get_nodes_a(self, x: str):
        return self.nodes[x]

    def getNeighbors(self, node):
        return self.edges[node]
