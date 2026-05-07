#The graph on the board feb 12
from Guttag14c import *

p = 'ABCDEFGH'
G = Digraph()
for name in p:
    G.add_node(Node(name))

G.add_edge(Edge(G._nodes[0], G._nodes[1]))
G.add_edge(Edge(G._nodes[5], G._nodes[7]))
G.add_edge(Edge(G.get_node_from_name('D'),G.get_node_from_name('E')) )