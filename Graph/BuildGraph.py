from ExtractorFactory.ExtractorSpawner import ExtractorSpawner


class BuildGraph():
    def __init__(self, graph):
        self.graph = graph

    def addEdge(self, row):
        if row['station1'] not in self.graph.edges:
            self.graph.edges[row['station1']] = [
                (row['station2'], row['time'], row['line'])]
        else:
            if (row['station2'], row['time'], row['line']
                    ) not in self.graph.edges[row['station1']]:
                self.graph.edges[row['station1']].append(
                    (row['station2'], row['time'], row['line']))

        if row['station2'] not in self.graph.edges:
            self.graph.edges[row['station2']] = [
                (row['station1'], row['time'], row['line'])]
        else:
            if (row['station1'], row['time'], row['line']
                    ) not in self.graph.edges[row['station2']]:
                self.graph.edges[row['station2']].append(
                    (row['station1'], row['time'], row['line']))

    def addNode(self, row):
        self.graph.nodes[row['id']] = (row['longitude'], row['latitude'])

    def addZone(self, row):
        if row['zone'] not in self.graph.zones:
            self.graph.zones[row['zone']] = [row['id']]
        else:
            self.graph.zones[row['zone']].append(row['id'])
