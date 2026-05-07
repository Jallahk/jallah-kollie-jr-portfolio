#Linked List Exercise
from LLclass import *

data1 = [23,11,88,62,2,90,21,67]
data2 = ['banana', 'apricot', 'apple','peach','plum', 'kiwi','mango']

#Using no other imports:

#1.  Make a linked list called L1 from the data in data1.

L1 = LinkedList(LLnode(data1[0]))

for i in data1:
    L1.addNode(LLnode(i))
    
    

print(L1) 
    








#2.	 Make a linked list called L2 from the data in data2.

L2 = LinkedList(LLnode(data2[0]))

for i in data2:
    L2.addNode(LLnode(i))
    
print(L2)  

#3.  Make function join(LL1,LL2) that attaches a linked list LL2 to the end of linked list LL1.

def join(LL1,LL2):
    current = LL2.first
    while current != LL2.last:
        LL1.addNode(current)
        current = current.nextNode
    LL1.addNode(current)
    
        
        
    
    
     
 


#4.  Make a function called shuffle(LL1,LL2) that alternately shuffles two linked lists into a new linked list.
#    For example,the first three nodes of shuffle(L1,L2) would have values 23,'banana',11.



#5.  Suppose that the values in a linked list represent the coefficients of a polynomial. For example,
# here is a linked list representation of x^3 - 2x^2 + 4x + 5




poly = LinkedList(LLnode(1))
for x in [-2,4,5]:
    poly.addNode(LLnode(x))
    
#   Write a function evalu(LL,x) that evaluates a polynomial represented as a linked list at the value x. For example,
#   evalu(poly,2) would return 13.



def evalu(LL,x):
    
    


