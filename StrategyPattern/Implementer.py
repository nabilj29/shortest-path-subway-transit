class Implementer:
    # make the context class of the strategy pattern

    def __init__(self):
        self.strategy = None

    def execute(self, startNode, stopNode):
        return self.strategy.algo(startNode, stopNode)

    def exceute(self, subnodes):
        return self.strategy.algo(subnodes)

    def setStrategy(self, strategy):
        self.strategy = strategy
