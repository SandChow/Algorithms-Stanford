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

    def are_connected(self, node1, node2):
        """ Checks whether two nodes are connected to each other 
            regardless of whether the graph is directed """

        if node1 in self._graph and node2 in self._graph:
            return node1 in self._graph[node2] or node2 in self._graph[node1]
        return False

    def find_path(self, node1, node2, path = []):
        """ Finds any path from node1 to node2 which may not be the shortest """
        
        current_path = path + [node1]
        if node1 == node2:
            return current_path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in current_path:
                new_path = self.find_path(node, node2, current_path)
                if new_path:
                    return new_path
        return None
