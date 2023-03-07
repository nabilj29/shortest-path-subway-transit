from abc import ABC, abstractmethod


class ExtractorFactoryInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def extractSpawner(self):
        pass
