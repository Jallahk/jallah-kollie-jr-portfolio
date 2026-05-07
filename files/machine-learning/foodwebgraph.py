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

#1.
print('There are {0} vertices.'.format(len(fw._nodes)))
#2.
ecount = 0
for node in fw._edges:
    ecount += len(fw._edges[node])
print('There are {0} edges.'.format(ecount))
#3.
scorpEats = len(fw._edges[fw.get_node_from_name('Scorpion')])
print('The scorpion eats {0} species.'.format(scorpEats))
#4.
def eats(animal:str):
    eatList = fw._edges[fw.get_node_from_name(animal)]
    return [a.get_name() for a in eatList]
#5.
eaters = 0
for node in fw._nodes:
    if fw.get_node_from_name('Blister Beetle') in fw._edges[node]:
        eaters +=1
print('{0} species eat the Blister Beetle.'.format(eaters))
#6.
def eaten(organism):
    eatenbylist =[]
    for animal in fw._nodes:
        if organism in eats(animal.get_name()):
            eatenbylist.append(animal.get_name())
    return eatenbylist

#7.
maxnum = 0
maxanimal =''
for animal in fw._nodes:
    animalname = animal.get_name()
    if len(eats(animalname)) > maxnum:
        maxnum = len(eats(animalname))
        maxanimal = animalname
print('{0} eats the most species.'.format(maxanimal))


#8
not_eaten = []
for animal in fw._nodes:
    if not eaten(animal.get_name()):
        not_eaten.append(animal.get_name)
        
print('The {0} is not eaten by any other animal.'.format(not_eaten))







