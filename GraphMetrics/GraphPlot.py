from matplotlib import pyplot as plt


class GraphPlot:

    def plot(self, Graph):
        plt.bar(Graph.degree.keys(), Graph.degree.values(), color='g')
        plt.xlabel('Degree')
        plt.ylabel('Number of Nodes')
        plt.title('Degree Distribution')
        plt.show()
