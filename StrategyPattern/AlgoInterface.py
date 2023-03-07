from abc import ABC, abstractmethod


class AlgoInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def algo(self, startNode, stopNode):
        pass

    @abstractmethod
    def resetKPI(self):
        pass
