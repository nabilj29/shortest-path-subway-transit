from abc import ABC, abstractmethod


class GraphMetrics(ABC):

    @abstractmethod
    def metric(self, Graph):
        pass
