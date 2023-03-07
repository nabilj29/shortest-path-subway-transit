from itertools import permutations
from ExtractorFactory.ExtractorSpawner import ExtractorSpawner
from Graph.GraphClass import GraphClass
from Graph.BuildGraph import BuildGraph
from StrategyPattern.Implementer import Implementer
from StrategyPattern.DijkstraAlgo import DijkstraAlgo


class tspalgo():
    def __init__(self, graph):
        self.graph = graph

    def algo(self, subnodes):
        # to generate graph must take input list of cities
        # into a matrix
        # Implement the strategy pattern made by the strategy pattern folder
        implementer = Implementer()
        implementer.setStrategy(DijkstraAlgo(self.graph))

        allPermutations = list(permutations(subnodes, len(subnodes)))
        minRoute = 999999999
        minRouteList = []
        visited = []
        reject = False
        for path in allPermutations:
            distance = 0
            reject = False
            visited = []
            currentPath = [path[0]]
            for i in range(len(path) - 1):
                if (path[i + 1] in visited):
                    continue
                data = implementer.execute(path[i], path[i + 1])
                distance += int(data[1])
                for i in range(1, len(data[0])):
                    if data[0][i] in visited:
                        reject = True
                        break
                    visited.append(data[0][i])
                    currentPath.append(data[0][i])
            if distance < minRoute:
                minRoute = distance
                minRouteList = currentPath
        if (len(minRouteList) == 0):
            return "No route found"
        else:
            return "The min time is " + \
                str(minRoute) + ", " + "taking the route" + str(minRouteList)

    def resetKPI(self):
        return super().resetKPI()
