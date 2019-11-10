import math
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def disjoint(lst1, lst2):
    lst1 = lst1.copy()
    for elem in lst2:
        if elem in lst1:
            lst1.remove(elem)
    return lst1

k = 2
G = nx.Graph(color="black")
lst = ["Rd","Bl"] * k
lst[0] = "B"
lst[1] = "P"

possible = list(itertools.permutations(lst, k))
print(len(possible))
count = 0
redWins =[]
blueWins = []
for c in possible:
    if "B" and "P" in c or not "B" and "P" in c:
        G.add_node(c, color="red")
        print(G.nodes[c])
    else:
        G.add_node(c, color="blue")

graph = {}
graph.fromkeys(possible)

for c in possible:
    OtherRoom = disjoint(lst, c)
    #print(lst)
    l = []
    #print(c)
    for elem1 in c:
        c2 = set(c).copy()
        c2.remove(elem1)
        #print(c2)
        for elem2 in OtherRoom:
            c3 = set(c2).copy()
            c3.add(elem2)
            if c3 not in l and len(c3) == k:
                l.append(set(c3))
        #print(len(graph[c]))
    graph[c] = l

print(graph)
for k in graph.keys():
    for state in graph[k]:
        G.add_edge(k, tuple(state))
#  print("%s : %s" % (k, graph[k]))
color_map = []

dfs = nx.dfs_tree(G)

for node in dfs.nodes:
    color = dfs.nodes[node]
    if color:
        print(color)
        color_map.append(color["color"])
    else: color_map.append("black")
nx.draw_shell(dfs,node_color=color_map, with_labels=True)


#nx.draw_shell(G, node_color=color_map, with_labels=False)

plt.savefig("tree.png", with_labels=True)
