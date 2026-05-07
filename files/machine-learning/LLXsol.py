#Linked List Exercise
from LLclass import *

data1 = [23,11,88,62,2,90,21,67]
data2 = ['banana', 'apricot', 'apple','peach','plum', 'kiwi','mango']

#Using no other imports:

#1.  Make a linked list called L1 from the data in data1.
L1 = LinkedList(LLnode(data1[0]))
for v in data1[1:]:
    L1.addNode(LLnode(v))

#2.	 Make a linked list called L2 from the data in data2.

L2 = LinkedList(LLnode(data2[0]))
for v in data2[1:]:
    L2.addNode(LLnode(v))

#3.  Make function join(LL1,LL2) that attaches a linked list LL2 to the end of linkd list LL1.
def join(LL1,LL2):
    current = LL2.first
    while current != LL2.last:
        LL1.addNode(current)
        current = current.nextNode
    LL1.addNode(current)

#or
def join2(LL1,LL2):
    vlist =[LL2.first.value]
    current = LL2.first.nextNode
    while current != LL2.last:
        vlist.append(current.value)
        current = current.nextNode
    vlist.append(current.value)
    for v in vlist:
        LL1.addNode(LLnode(v))
    

#4.  Make a function called shuffle(LL1,LL2) that alternately shuffles two linked lists into a new linked list.
#    For example,the first three nodes of shuffle(L1,L2) would have values 23,'banana',11.
def shuffle(LL1,LL2):
    
    def getNodeValues(L):  #Makes a list of node values
        getv =[]
        current = L.first
        while current != L.last:
            getv.append(current.value)
            current = current.nextNode
        getv.append(current.value)
        return getv
    
    getv1 = getNodeValues(LL1)
    getv2 = getNodeValues(LL2)
    
    LLS = LinkedList(LLnode(getv1[0]))
    LLS.addNode(LLnode(getv2[0]))
    
    shortest = min(len(getv1),len(getv2))
    
    for i in range(1,shortest):
        LLS.addNode(LLnode(getv1[i]))
        LLS.addNode(LLnode(getv2[i]))
    
    r1 = len(getv1)-shortest
    r2 = len(getv2)-shortest
    
    if r1 != 0:
        for i in range(shortest,len(getv1)):
            LLS.addNode(LLnode(getv1[i]))
    if r2 != 0:
        for i in range(shortest,len(getv2)):
            LLS.addNode(LLnode(getv2[i]))
    
    return LLS
    
        
    


#5.  Suppose that the values in a linked list represent the coefficients of a polynomial. For example,
# here is a linked list representation of x^3 - 2x^2 + 4x + 5

poly = LinkedList(LLnode(1))
for x in [-2,4,5]:
    poly.addNode(LLnode(x))
    
#   Write a function evalu(LL,x) that evaluates a polynomial represented as a linked list at the value x. For example,
#   evalu(poly,2) would return 13.

def evalu(poly,x):
    val = 0
    pow = poly.nodeCount
    current = poly.first
    while current != poly.last:
        val += current.value * x **pow
        current = current.nextNode
        pow =pow -1
    val += current.value
    return val
        
    
