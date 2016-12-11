from Graph import Graph
from pprint import pprint

if __name__=="__main__":
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    x = Graph(connections)
    print x
    print x.are_connected('B', 'C')
    print x.find_path('C', 'D')
