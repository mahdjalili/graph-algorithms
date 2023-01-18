import graph
import dijkstra
import prim
import kruskal
import tsp

g = graph.Graph(7, False)
g.add_edge(0, 1, 7)
g.add_edge(0, 3, 5)

g.add_edge(1, 2, 8)
g.add_edge(1, 4, 7)
g.add_edge(1, 3, 9)

g.add_edge(2, 4, 5)

g.add_edge(3, 4, 15)
g.add_edge(3, 5, 6)

g.add_edge(4, 5, 8)
g.add_edge(4, 6, 9)

g.add_edge(5, 6, 11)

alg = None
while alg != "end":
    print("\n1 - Prim\n2 - Kruskal\n3 - Dijkstra\n4 - TSP\nOr type \"end\"!\n")
    alg = input("Chose your algorithm: ")

    if alg == "1":
        prim.prim(g)
    elif alg == "2":
        kruskal.kruskal(g)
    elif alg == "3":
        dijkstra.dijkstra(g, 0, 6)
    elif alg == "4":
        tsp.tsp(g, 0)
    elif alg == "end":
        print("Bye :)")
    else:
        print("Wrong Choice!")
