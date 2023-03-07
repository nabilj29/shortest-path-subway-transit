from GraphMetrics.GraphMetrics import GraphMetrics


class degreeMetric(GraphMetrics):
    def __init__(self):
        super().__init__()

    def metric(self, Graph):
        for key in Graph.edges:
            if len(Graph.edges[key]) in Graph.degree:
                Graph.degree[len(Graph.edges[key])] += 1
            else:
                Graph.degree[len(Graph.edges[key])] = 1
        return Graph.degree
