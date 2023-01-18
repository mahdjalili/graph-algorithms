import sys


def min_key(graph, key, visited):
    min = sys.maxsize

    for v in range(graph.vertices):
        if key[v] < min and visited[v] == False:
            min = key[v]
            min_index = v

    return min_index


def prim(graph):
    print("\nPrim's Algorithm:")

    key = [sys.maxsize] * graph.vertices
    key[0] = 0

    parent = [None] * graph.vertices
    parent[0] = -1

    visited = [False] * graph.vertices

    for count in range(graph.vertices):

        u = min_key(graph, key, visited)
        print(u, end=" => ")

        visited[u] = True

        for v in range(graph.vertices):

            if graph.edges[u][v] > 0 and visited[v] == False and key[v] > graph.edges[u][v]:
                key[v] = graph.edges[u][v]
                parent[v] = u

    print("\nEdge \tWeight")
    for i in range(1, graph.vertices):
        print("%d - %d \t %d" % (i, parent[i], graph.edges[parent[i]][i]))

    return graph
