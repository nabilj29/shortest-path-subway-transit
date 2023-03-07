from ExtractorFactory.ExtractorFactoryInterface import ExtractorFactoryInterface
from ExtractorFactory.ConcreteExtractor1 import ConcreteExtractor1


class ExtractorSpawner(ExtractorFactoryInterface):
    def __init__(self):
        super().__init__()

    def extractSpawner(
            self,
            type,
            csvfileConnection,
            csvfileNode,
            graphBuilder):
        if type == 'ConcreteExtractor1':
            return ConcreteExtractor1(
                csvfileConnection, csvfileNode, graphBuilder)
