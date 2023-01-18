from sys import maxsize
from itertools import permutations


def tsp(graph, s):

    print("\nTSP algorithm:")

    vertex = []
    for i in range(graph.vertices):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph.edges[k][j]
            k = j
        current_pathweight += graph.edges[k][s]

        min_path = min(min_path, current_pathweight)

    print("minimum path weight for travel all edges and back to first place again is:", min_path)
