import math
import itertools
import networkx as nx

def disjoint(lst1, lst2):
    lst1 = lst1.copy()
    for elem in lst2:
        if elem in lst1:
            lst1.remove(elem)
    return lst1

k = 3
G = nx.Graph()
lst = ["Rd","Bl"] * k
lst[0] = "B"
lst[1] = "P"

possible = list(itertools.combinations(lst, k))

count = 0
redWins =[]
blueWins = []
for c in possible:
    if "B" and "P" in c:
        redWins.append(c)
        G.add_node(c, color="red")
    else:
        blueWins.append(c)
        G.add_node(c, color="blue")

graph = {}
graph.fromkeys(possible)

for c in possible:
    OtherRoom = disjoint(lst, c)
    #print(lst)
    l = []
    #print(c)
    for elem1 in c:
        c2 = list(c).copy()
        c2.remove(elem1)
        #print(c2)
        for elem2 in OtherRoom:
            c3 = list(c2).copy()
            c3.append(elem2)
            if c3 not in l:
                l.append(tuple(c3))
        #print(len(graph[c]))
    graph[c] = l

for k in graph.keys():
    for state in graph[k]:
        g = graph[k].copy()
        g.remove(state)
        for s in g:
            if s is state:
                graph[k].remove(s)
        G.add_edge(k,tuple(graph[k]))
    #print("%s : %s" % (k, graph[k]))

traversal = nx.dfs_tree(G, G.nodes[0])

