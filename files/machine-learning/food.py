#FoodWeb Graph

from Guttag14c import *

fw = Digraph()
infile = open('foodweb.txt','r')
for line in infile:
    LL = line[:-1].split('->')
    sname = LL[0]
    dname = LL[1]
    if not fw.get_node_from_name(sname):
        fw.add_node(Node(sname))
    sNode = fw.get_node_from_name(sname)
    if not fw.get_node_from_name(dname):
        fw.add_node(Node(dname))
    dNode = fw.get_node_from_name(dname)
    if dNode not in fw._edges[sNode]:
        fw._edges[sNode].append(dNode)   
        

infile.close()
#1
print(len(fw._nodes))


#2
numOfEdge = 0    
for node in fw._edges:
    numOfEdge += len(fw._edges[node])
         
print(numOfEdge)


# 3

scorpion = len(fw._edges[fw.get_node_from_name('Scorpion')])
print(scorpion)


#4

def animal(eat:str):
    aniList = fw._edges[fw.get_node_from_name(eat)]
    return [i.get_name() for i in aniList]



animal('Scorpion')


#5
eater = 0
for node in fw._nodes:
    if fw.get_node_from_name('Blister Beetle') in fw._edges[node]:
        eater +=1
    
print(eater)

#6

def prey(org: str):
    
    for ani in fw._nodes:
        eatList = []
        if org in animal(ani.get_name()):
            
        
            eatList.append(ani.get_name())
        
    return eatList
    

    
#7
maxnum = 18
maxanmal = ''
for animal in fw._nodes:
    animalname = animal.get_name()
    if len(eats(animalname)) > maxnum:
        maxnum = len(eats(animalname))
        maxanimal = animalname
        
print('{0} eats the most species.'.format(maxanimal))

   

