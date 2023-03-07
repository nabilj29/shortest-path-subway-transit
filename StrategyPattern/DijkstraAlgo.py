from StrategyPattern.AlgoInterface import AlgoInterface


class DijkstraAlgo(AlgoInterface):
    def __init__(self, graph):
        super().__init__()
        self.edges = graph.edges
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def algo(self, start, end):
        # initialize the distances to infinity
        distances = {}
        for node in self.edges:
            self.iterations += 1
            self.dataAccess += 1
            distances[node] = float('inf')
        # initialize the previous nodes to None
        previous = {}
        for node in self.edges:
            self.iterations += 1
            self.dataAccess += 1
            previous[node] = None
        # initialize the unvisited nodes to all nodes
        unvisited = {}
        for node in self.edges:
            self.iterations += 1
            self.dataAccess += 1
            unvisited[node] = True
        # set the distance to the start node to 0
        self.dataAccess += 1
        distances[start] = 0
        # while there are still unvisited nodes
        self.comparisons += 1
        while len(unvisited) > 0:
            self.iterations += 1
            self.comparisons += 1
            # find the unvisited node with the smallest distance
            current = None
            for node in unvisited:
                self.iterations += 1
                self.comparisons += 2
                self.dataAccess += 2
                if current is None:
                    current = node
                elif distances[node] < distances[current]:
                    current = node
            # if the smallest distance is infinity, we are done
            self.comparisons += 1
            self.dataAccess += 1
            if distances[current] == float('inf'):
                break

            # remove the current node from the unvisited nodes
            self.dataAccess += 1
            del unvisited[current]
            # for each neighbor of the current node
            self.dataAccess += 1
            for neighbor in self.edges[current]:
                self.iterations += 1
                self.dataAccess += 1
                # if the neighbor is unvisited
                self.comparisons += 1
                self.dataAccess += 1
                if neighbor[0] in unvisited:
                    # calculate the distance through the current node
                    self.dataAccess += 2
                    new_distance = distances[current] + int(neighbor[1])
                    # if the distance through the current node is smaller than
                    # the current distance
                    self.comparisons += 1
                    self.dataAccess += 1
                    if new_distance < distances[neighbor[0]]:
                        # update the distance
                        self.dataAccess += 2
                        distances[neighbor[0]] = new_distance
                        # update the previous node
                        previous[neighbor[0]] = current
        # initialize the path
        path = []
        # set the current node to the end node
        current = end
        # while the current node is not None
        self.comparisons += 1
        while current is not None:
            self.comparisons += 1
            self.iterations += 1
            # add the current node to the path
            path.append(current)
            # set the current node to the previous node
            self.dataAccess += 1
            current = previous[current]
        # reverse the path
        path.reverse()
        # return the path and the distance
        self.dataAccess += 1
        return path, distances[end]

    def resetKPI(self):
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0
