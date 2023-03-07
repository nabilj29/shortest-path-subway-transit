import csv
from ExtractorFactory.ExtractorInterface import ExtractorInterface
from GraphMetrics.degreeMetric import degreeMetric


class ConcreteExtractor1(ExtractorInterface):
    def __init__(self, csvfileConnection, csvfileNode, graphBuilder):
        super().__init__()
        self.csvfileConnection = csvfileConnection
        self.csvfileNode = csvfileNode
        self.graphBuilder = graphBuilder
        self.run()

    def extractEdge(self):
        # Read in the data from the csv file
        with open(self.csvfileConnection, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.graphBuilder.addEdge(row)

    def extractNode(self):
        with open(self.csvfileNode, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.graphBuilder.addNode(row)

    def extractZones(self):
        with open(self.csvfileNode, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.graphBuilder.addZone(row)

    def run(self):
        self.extractEdge()
        self.extractNode()
        self.extractZones()
        degreeMetric().metric(self.graphBuilder.graph)
