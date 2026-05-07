from Guttag14c import *

infile = open('g1.txt','r')
g1 = Digraph()

for line in infile:
    parts = line[:-1].split(',')
    
    if not g1.get_node_from_name(parts[0]):
        srt = Node(parts[0])
        g1.add_node(srt)
        
    if not g1.get_node_from_name(parts[1]):
        end = Node(parts[1])
        g1.add_node(end)
        
    if g1.get_node_from_name(parts[1]) not in g1._edges[g1.get_node_from_name(parts[0])]:
        g1.add_edge(Edge(,end))
        
        

    
    
    
infile.close()




#print(parts)