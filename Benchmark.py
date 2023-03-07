import time
import random

from matplotlib import pyplot as plt
from ExtractorFactory.ExtractorSpawner import ExtractorSpawner
from Graph.GraphClass import GraphClass
from Graph.BuildGraph import BuildGraph
from StrategyPattern.Implementer import Implementer
from StrategyPattern.AStarAlgo import AStarAlgo
from StrategyPattern.DijkstraAlgo import DijkstraAlgo


class Benchmark:
    def __init__(self, graph):
        self.graph = graph
        self.implementer = Implementer()
        self.stationsList = list(self.graph.nodes.keys())
        random.seed(1659644754)
        self.dataset = {
            "10": [],
            "50": [],
            "100": [],
            "200": [],
            "300": [],
            "400": [],
            "500": [],
            "600": [],
            "700": [],
            "800": [],
            "900": [],
            "1000": [],
            "1500": [],
            "2000": [],
            
            
        }

        for i in self.dataset:
            for j in range(int(i)):
                self.dataset[i].append(
                    [random.choice(self.stationsList), random.choice(self.stationsList)])

    def benchmark(self, algo):

        resultIteration = {}
        resultDataAccess = {}
        resultComparison = {}
        resultTime = {}
        totalOperations = {}

        print("Benchmarking for " + algo + "...")
        if algo == "AStar":
            aStar = AStarAlgo(self.graph)
            self.implementer.setStrategy(aStar)
        elif algo == "Dijkstra":
            dijksta = DijkstraAlgo(self.graph)
            self.implementer.setStrategy(dijksta)

        for i in self.dataset:
            start = time.time()
            for j in self.dataset[i]:
                self.implementer.execute(j[0], j[1])
            totalTime = time.time() - start

            totalOperations[i] = self.implementer.strategy.iterations + \
                self.implementer.strategy.dataAccess + \
                self.implementer.strategy.comparisons
            resultIteration[i] = self.implementer.strategy.iterations
            resultDataAccess[i] = self.implementer.strategy.dataAccess
            resultComparison[i] = self.implementer.strategy.comparisons
            resultTime[i] = totalTime

            print("\nRumtime for", i, "loop",
                  "(" + algo + ")" + ":", totalTime, "seconds")
            print("Iteration (KPI) count for", i, "loops",
                  "(" + algo + ")" + ":", self.implementer.strategy.iterations)
            print("Data Access (KPI) count for", i, "loops",
                  "(" + algo + ")" + ":", self.implementer.strategy.dataAccess)
            print(
                "Comparison (KPI) count for",
                i,
                "loops",
                "(" + algo + ")" + ":",
                self.implementer.strategy.comparisons)
            print("Total Operations (KPI) count for", i, "loops",
                  "(" + algo + ")" + ":", totalOperations[i])

            self.implementer.strategy.resetKPI()

        return totalOperations, resultTime, resultIteration, resultDataAccess, resultComparison

    def graphBenchMark(
            self,
            dTotalOperation,
            dIteration,
            dDataAccess,
            dComparison,
            dTime,
            aTotalOperation,
            aIteration,
            aDataAccess,
            aComparison,
            aTime):

        plt.xlabel('array size')
        plt.ylabel('Iterations')
        plt.title("Iterations Comparison")
        plt.plot([x for x in dIteration.keys()], [
            x for x in dIteration.values()], '--bo', label='Dijkstra')
        plt.plot([x for x in aIteration.keys()], [
            x for x in aIteration.values()], '--ro', label='AStar')
        plt.legend()
        plt.show()

        plt.xlabel('array size')
        plt.ylabel('Data Access')
        plt.title("Data Access Comparison")
        plt.plot([x for x in dDataAccess.keys()], [
            x for x in dDataAccess.values()], '--bo', label='Dijkstra')
        plt.plot([x for x in aDataAccess.keys()], [
            x for x in aDataAccess.values()], "--ro", label='AStar')
        plt.legend()
        plt.show()

        plt.xlabel('array size')
        plt.ylabel('Comparison')
        plt.title("Comparison Comparison")
        plt.plot([x for x in dComparison.keys()], [
            x for x in dComparison.values()], '--bo', label='Dijkstra')
        plt.plot([x for x in aComparison.keys()], [
            x for x in aComparison.values()], "--ro", label='AStar')
        plt.legend()
        plt.show()

        plt.xlabel('array size')
        plt.ylabel('Time')
        plt.title("Time Comparison")
        plt.plot([x for x in dTime.keys()], [
            x for x in dTime.values()], '--bo', label='Dijkstra')
        plt.plot([x for x in aTime.keys()], [
            x for x in aTime.values()], "--ro", label='AStar')
        plt.legend()
        plt.show()

        plt.xlabel('array size')
        plt.ylabel('Total Operations')
        plt.title("Total Operations Comparison")
        plt.plot([x for x in dTotalOperation.keys()], [
            x for x in dTotalOperation.values()], '--bo', label='Dijkstra')
        plt.plot([x for x in aTotalOperation.keys()], [
            x for x in aTotalOperation.values()], '--ro', label='AStar')
        plt.legend()
        plt.show()
