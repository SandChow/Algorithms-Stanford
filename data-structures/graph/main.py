from Graph import Graph
from pprint import pprint

if __name__=="__main__":
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    x = Graph(connections)
    print x
    x.remove('B')
    print x
