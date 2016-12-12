from Graph import Graph
from pprint import pprint

if __name__=="__main__":
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C'), ('Y', 'Z'), ('S', 'X')]
    directed = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
    x = Graph(connections)
    y = Graph(directed, True)
    #print x
    #print x.are_connected('B', 'C')
    #print x.find_path('C', 'D')
    """
    print x.find_shortest_path('A', 'E')
    print x.connected_components()
    print y
    print y.in_degree("D")
    y.topological_sort()
    print x.number_of_nodes
    """
    z = Graph([('A', 'K'), ('A', 'C'), ('K', 'E'), ('K', 'F')])
    print z 
    print z.bfs("A")
    print z.dfs("A")
    print z.dfs_loop("A")

