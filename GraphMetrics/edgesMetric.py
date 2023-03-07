from GraphMetrics.GraphMetrics import GraphMetrics


class edgesMetric(GraphMetrics):
    def __init__(self):
        super().__init__()

    def metric(self, GraphClass):
        return GraphClass.edges
