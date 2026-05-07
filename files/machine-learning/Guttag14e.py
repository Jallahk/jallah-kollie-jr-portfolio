from Guttag14c import *
# # Figure 14-11 on page 303
def BFS(graph, start, end, to_print = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        #Get and remove oldest element in path_queue
        tmp_path = path_queue.pop(0)
        if to_print:
            print('Current BFS path:', print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None

# # test_sp modifed as per code on page 303
def test_SP():
    nodes = []
    for name in range(6): #Create 6 nodes
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0],nodes[1]))
    g.add_edge(Edge(nodes[1],nodes[2]))
    g.add_edge(Edge(nodes[2],nodes[3]))
    g.add_edge(Edge(nodes[2],nodes[4]))
    g.add_edge(Edge(nodes[3],nodes[4]))
    g.add_edge(Edge(nodes[3],nodes[5]))
    g.add_edge(Edge(nodes[0],nodes[2]))
    g.add_edge(Edge(nodes[1],nodes[0]))
    g.add_edge(Edge(nodes[3],nodes[1]))
    g.add_edge(Edge(nodes[4],nodes[0]))
    sp = shortest_path(g, nodes[0], nodes[5], to_print = True)
    print('Shortest path found by DFS:', print_path(sp))
    sp = BFS(g, nodes[0], nodes[5], to_print = True)
    print('Shortest path found by BFS:', print_path(sp))

# test_SP()
