from ExtractorFactory.ExtractorSpawner import ExtractorSpawner
from Graph.GraphClass import GraphClass
from Graph.BuildGraph import BuildGraph
from StrategyPattern.Implementer import Implementer
from StrategyPattern.AStarAlgo import AStarAlgo
from StrategyPattern.DijkstraAlgo import DijkstraAlgo


class Itinerary:
    def __init__(self, graph):
        self.graph = graph

        # Implement the strategy pattern made by the strategy pattern folder
        self.implementer = Implementer()

    def showItinerary(self, station1, station2):
        returnVal = ""
        self.implementer.setStrategy(AStarAlgo(self.graph))
        returnVal += "A Star Route"
        routeA = self.implementer.execute(station1, station2)
        routeALines = self.getLines(routeA[0])
        returnVal += str(routeA[0]) + "\n"
        returnVal += "Total time: " + str(routeA[1]) + "\n"
        returnVal += "Total connections: " + str(len(routeA[0])) + "\n"
        returnVal += "Lines: " + \
            str(routeALines) + "\n"

        returnVal += "\nDijkstra Route" + "\n"
        self.implementer.setStrategy(DijkstraAlgo(self.graph))
        routeD = self.implementer.execute(station1, station2)
        routeDLines = int(self.getLines(routeD[0]))
        returnVal += str(routeD[0]) + "\n"
        returnVal += "Total time:" + str(float(routeD[1])) + "\n"
        returnVal += "Total connections: " + str(len(routeD[0])) + "\n"
        returnVal += "Lines: " + \
            str(routeDLines) + "\n" + "\n"

        returnVal += "-----Results-----\n"

        if routeA[1] < routeD[1]:
            returnVal += "A Star Route is the best because it takes less time than the Dijkstra Route by", routeD[
                1] - routeA[1], "\n"
        elif routeA[1] > routeD[1]:
            returnVal += "Dijkstra Route is the best because it takes less time than the A Star Route by", routeA[
                1] - routeD[1], "\n"
        else:
            if int(routeALines < routeDLines):
                returnLine = str(routeDLines - routeALines)
                returnVal += "A Star Route is the best because it takes less lines than the Dijkstra Route by"
                returnVal += returnLine + "\n"
            elif int(routeALines) > int(routeDLines):
                returnLine = str(routeALines - routeDLines)
                returnVal += "Dijkstra Route is the best because it takes less lines than the A Star Route by: "
                returnVal += returnLine + "\n"
            else:
                if len(routeA[0]) < len(routeD[0]):
                    returnVal += "A Star Route is the best because it takes less connections than the Dijkstra Route by", len(
                        routeD[0]) - len(routeA[0]), "\n"
                elif len(routeA[0]) > len(routeD[0]):
                    returnVal += "Dijkstra Route is the best because it takes less connections than the A Star Route by", len(
                        routeA[0]) - len(routeD[0]), "\n"
                else:
                    returnVal += "Either route work fine as both have same time, number of lines, and connections" + "\n"
        returnVal += "-----------------\n"
        return returnVal

    def getLines(self, route):
        lines = []
        for i in range(len(route) - 1):
            for j in range(len(self.graph.edges[route[i]])):
                if self.graph.edges[route[i]][j][0] == route[i + 1]:
                    lines.append(self.graph.edges[route[i]][j][2])
        return len(set(lines))
