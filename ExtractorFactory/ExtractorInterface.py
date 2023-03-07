from abc import ABC, abstractmethod


class ExtractorInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extractEdge(self):
        pass

    @abstractmethod
    def extractNode(self):
        pass

    @abstractmethod
    def run(self):
        pass
