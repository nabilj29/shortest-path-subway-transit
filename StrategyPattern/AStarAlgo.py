from StrategyPattern.AlgoInterface import AlgoInterface


class AStarAlgo(AlgoInterface):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0

    def heuristic(self, x, y):
        hInput1 = abs(
            float(
                self.graph.get_nodes_a(x)[0]) -
            float(
                self.graph.get_nodes_a(y)[0]))
        hInput2 = abs(
            float(
                self.graph.get_nodes_a(x)[1]) -
            float(
                self.graph.get_nodes_a(y)[1]))
        h = hInput1 + hInput2
        self.dataAccess += 8

        return h

    def algo(self, startNode, stopNode):
        openNodes = {startNode}
        closedNodes = set()
        # distance from start node
        distanceStart = {}
        # parent has adjacent node
        parents = {}
        # distance of starting node from itself is zero
        distanceStart[startNode] = 0
        self.dataAccess += 1
        # so startnode is its own parent
        parents[startNode] = startNode
        self.dataAccess += 1
        self.comparisons += 1
        while len(openNodes) > 0:
            self.iterations += 1
            self.comparisons += 1
            n = None

            for y in openNodes:
                self.iterations += 1
                self.dataAccess += 2
                self.comparisons += 2
                if n is None or distanceStart[y] + self.heuristic(
                        y, stopNode) < distanceStart[n] + self.heuristic(n, stopNode):
                    n = y
            self.comparisons += 1
            if n == stopNode:
                pass
            else:
                self.dataAccess += 1
                for (m, weight, line) in self.graph.getNeighbors(n):
                    self.iterations += 1
                    # n is set its parent
                    self.comparisons += 2
                    if m not in openNodes and m not in closedNodes:
                        openNodes.add(m)
                        parents[m] = n
                        distanceStart[m] = float(
                            distanceStart[(n)]) + float(weight)
                        self.dataAccess += 3

                    # compare m for each node in open set
                    # whic is the distance from start to n node
                    else:
                        self.dataAccess += 2
                        self.comparisons += 1
                        if distanceStart[m] > distanceStart[n] + float(weight):
                            # update g(m)
                            distanceStart[m] = distanceStart[n] + float(weight)
                            # change parent of m to n
                            parents[m] = n
                            # if m in closed set,remove and add to open
                            if m in closedNodes:
                                closedNodes.remove(m)
                                openNodes.add(m)
                            self.dataAccess += 3
                            self.comparisons += 1

            self.comparisons += 1
            if n is None:
                print('No Path Exists!')
                return None

            # begin reconstructing path from goal to start
            # if current node is stopNode
            self.comparisons += 1
            if n == stopNode:
                path = []
                self.dataAccess += 1
                self.comparisons += 1
                while parents[n] != n:
                    self.comparisons += 1
                    self.iterations += 1
                    path.append(n)
                    n = parents[n]
                    self.dataAccess += 2
                path.append(startNode)
                path.reverse()
                self.dataAccess += 1
                return path, distanceStart[stopNode]

            # remove n from the openNodes, and add it to closedNodes
            # because all of his neighbors were checked
            openNodes.remove(n)
            closedNodes.add(n)
        print('Path does not exist!')
        return None

    def resetKPI(self):
        self.iterations = 0
        self.comparisons = 0
        self.dataAccess = 0
