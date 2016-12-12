from collections import defaultdict
from collections import deque

class Graph(object):
    """ A graph that is undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)
        self.number_of_nodes = len(sum(self.connected_components(), []))

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

    def find_shortest_path(self, node1, node2, path=[]):
        """ Finds shortest path from node1 to node2 """
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        shortest_path = None 
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_shortest_path(node, node2, path)
                if new_path:
                    if not shortest_path or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        return shortest_path

    def connected_components(self):
        components = []
        keys = self._graph.keys()
        if keys: 
            explored = []
            for i in keys:
                if i not in explored:
                    current_components = self.bfs(i)
                    explored += current_components
                    components.append(current_components)
        return components

    def in_degree(self, node):
        incoming_edges = 0
        values = self._graph.values()
        for group in values:
            for value in group:
                if node is value:
                    incoming_edges += 1
        return incoming_edges


    def topological_sort(self):
        """ Worked on directed graphs. Error if cyclic! """

        all_connected_nodes = self.bfs(self._graph.keys()[0])
        in_degree_list= []
        zeros = 0
        for node in all_connected_nodes:
            count = self.in_degree(node)
            if count == 0:
                zeros += 1
            in_degree_list.append((node, count))
        if zeros is 0:
            raise RuntimeError("Not a directed acyclic graph (DAG)")
        print in_degree_list

    def bfs(self, root):
        if root:
            explored, queue = [root], deque([root])
            while queue:
                current_node = queue.popleft()
                for connection in self._graph[current_node]:
                    if connection not in explored:
                        explored.append(connection)
                        queue.append(connection)
            return explored

    def dfs(self, root, explored=[]):
        if root:
            explored.append(root)
            for connection in self._graph[root]:
                if connection not in explored:
                    self.dfs(connection, explored)
            return explored
