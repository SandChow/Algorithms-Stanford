from collections import defaultdict

class Graph(object):
    """ A graph that is undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs like 
            [('A', 'B'), ('B', 'C')]) to the graph. """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to the node. """

        for connections in self._graph.values():
            try:
                connections.remove(node)
            except KeyError:
                pass

            try:
                del self._graph[node]
            except KeyError:
                pass
