import sys


def min_distance(graph, dist, visited):
    min = sys.maxsize

    for v in range(graph.vertices):
        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_index = v

    return min_index


def dijkstra(graph, start, end):
    print("\nDijkstra's Algorithm:")
    distance = [sys.maxsize] * graph.vertices
    distance[start] = 0

    visited = [False] * graph.vertices

    for cout in range(graph.vertices):
        x = min_distance(graph, distance, visited)
        print(x, end=" => ")
        visited[x] = True

        for y in range(graph.vertices):
            if graph.edges[x][y] > 0 and visited[y] == False and distance[y] > distance[x] + graph.edges[x][y]:
                distance[y] = distance[x] + graph.edges[x][y]

    print("\nShortest distance from vertex ", start,
          " to vertex ", end, " is ", distance[end])
