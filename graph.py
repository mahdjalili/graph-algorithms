class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed

        self.edges = [[0 for column in range(self.vertices)]
                      for row in range(self.vertices)]

        self.list_edges = []

    def add_edge(self, node1, node2, weight=1):

        self.edges[node1][node2] = weight
        self.list_edges.append([node1, node2, weight])

        if not self.directed:
            self.edges[node2][node1] = weight
            self.list_edges.append([node2, node1, weight])

    def print_edges(self):
        print(self.edges, "\n", self.list_edges)
