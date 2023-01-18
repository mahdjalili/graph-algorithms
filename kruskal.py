def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(graph):
    print("\nKruskal's Algorithm:")
    result = []

    i = 0

    e = 0

    graph.list_edges = sorted(graph.list_edges,
                              key=lambda item: item[2])

    parent = []
    rank = []

    for node in range(graph.vertices):
        parent.append(node)
        rank.append(0)

    while e < graph.vertices - 1:

        u, v, w = graph.list_edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    minimumCost = 0
    print("Edge \tWeight")
    for u, v, weight in result:
        minimumCost += weight
        print("%d - %d \t %d" % (u, v, weight))
    print("Minimum Spanning Tree", minimumCost)
