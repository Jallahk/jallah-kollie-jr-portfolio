''' Jallah Kollie, Exam 1, Feb. 24 2025'''
import matplotlib.pyplot as plt
from Guttag14c import *
from Guttag14d import *
#1
social = Digraph()
#reads the file 
infile = open('people.txt', 'r')

#loops through the line file 
for line in infile:
    ppl = line[:-1].split('->')
    
    #start bode
    sname = ppl[0]
    #end node
    ename = ppl[1]
    #check if the sname node exist
    if not social.get_node_from_name(sname):
        social.add_node(Node(sname))
    
    #this assigns the sname in the grapgh to sNode 
    sNode = social.get_node_from_name(sname)
    
    
    #check if the ename node exist
    if not social.get_node_from_name(ename):
        social.add_node(Node(ename))
    
    #this assigns the sname in the grapgh to sNode 
    eNode = social.get_node_from_name(ename)
    
    #checks if sNode and eNode have and appends dNode to sNode edge list if not
    if eNode not in social._edges[sNode]:
        social._edges[sNode].append(eNode)


infile.close() 
    

#2

#node_outgoing_counts = {node.get_name(): len(social._edges[node]) for node in social._nodes}
nCount={}
for node in social._nodes:
    nCount[node.get_name()] = len(social._edges[node])
    
def barGraph():
#     create a dictionary to store the names and their edges        
    #sorts the list by turning it into a tupple and sort in ascending order    
    sorted_nodes = sorted(nCount.items(), key=lambda x: x[1])  # Sort by count (ascending)

#Extract sorted keys (node names) and values (counts)
    sorted_names, sorted_counts = zip(*sorted_nodes)  # Unpack into two lists
   
   #creates the graph
    plt.figure(figsize=(10, 6))
    plt.bar(sorted_names, sorted_counts, color ='blue')
    
    plt.ylabel('Number of people liked')
    plt.xlabel('Person')
    plt.title('Exam 1')
    
    plt.show()
 



#3
#finds the max value with in the nCount dict
max_ppl = max(nCount.values())
max_lis = []
#checks if more than one node has a max value
for node,count in nCount.items():
    if count == max_ppl:
        #add nodes with the max vals to the list
        max_lis.append(node)
        
    
print('The most amiable person is {0}'.format(','.join(max_lis)))

#finds the min value with in the nCount dict
min_ppl = min(nCount.values())
min_lis = []
#checks if more than one node has a max value
for node,count in nCount.items():
    if count == min_ppl:
        #add nodes with the max vals to the list
        min_lis.append(node)
        

print('The least amiable person is {0}'.format(','.join(min_lis)))

#4

#initialize a list and assign nodes as key and a value of 0

likes = {node.get_name(): 0 for node in social._nodes}

#loops through the nodes
for node in social._edges:
    #add 1 to value when a key is seen
    for person in social._edges[node]:
        likes[person.get_name()]+=1
        
#find the max likes         
max_likes = max(likes.values())

#finds the most popular person
popular = [cool for cool, peeps in likes.items() if peeps == max_likes]

print('The most popular person is {0}'.format(','.join(popular)), 'with the max of {0} likes!'.format( max_likes))


#5


def shortPath(graph,p1:str,p2:str):
    #gets the node name
   n1 = social.get_node_from_name(p1)
   n2 = social.get_node_from_name(p2)
   path1 = shortest_path(graph, n1,n2,False)
   
   #finds the shortest path
   path2 = shortest_path(graph, n2,n1,False)
   
   #returns the length of the shortest path
   if len(path1) > len(path2):
       length = len(path2) - 1
   else:
     length = len(path1) - 1
     
   print('The social distance between ', p1,'and', p2, 'is', length)
    
  

#print(social)
shortPath(social,'Ad','Ga')





#6

def clique():
    subset = str(input('what is your subset? Input names seperated by commas without {}. DO NOT USE " ", EX: Ad,Bo,Ca ')).split(',')
    print(subset)
    subset = [name.strip() for name in subset]
            
    node_name = [social.get_node_from_name(node) for node in subset]
#     print(node_name)
    for i in range(len(node_name)):
        for j in range(i+1,len(node_name)):
            node1 = node_name[i]
            node2 = node_name[j]
            
            #print(node1,node2)
            
            if node2 not in social._edges[node1] or node1 not in social._edges[node2]:
                print('This is not a clique')
                return
                
    print('This is a Clique')
            
clique()

#7
def find_maximal_clique(graph):
    """Find a maximal clique in the social graph."""
    all_nodes = graph._nodes  # ensure this retrieves the list of nodes
    
   

    maximal_clique = []
    
    for i in range(len(all_nodes)):
        clique_candidate = [all_nodes[i]]  # start a clique with one node

        for j in range(len(all_nodes)):
            if i != j:  # stops self comparison
                node1 = all_nodes[i]
                node2 = all_nodes[j]
                
                # check if node2 is connected to all nodes in the current clique_candidate
                if all(node2 in graph._edges[n] for n in clique_candidate):
                    clique_candidate.append(node2)

        # Update maximal_clique if the new clique_candidate is larger
        if len(clique_candidate) > len(maximal_clique):
            maximal_clique = clique_candidate

    # Convert Node objects to names before returning
    return [node.get_name() for node in maximal_clique]



max_clique = find_maximal_clique(social)
print("Maximal Clique:", max_clique)    


barGraph()




        