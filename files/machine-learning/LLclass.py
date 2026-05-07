#Introduction to Linked Lists


class LLnode(object):
    """A node is initialized with its value. Its head and tail are initialized as None"""
    def __init__(self,value):
        self.head=None
        self.tail=None
        self.value=value
    
    def __str__(self):
        return str(self.head)+' | '+str(self.value)+' | '+str(self.tail)+'\n'
        
    
class LinkedList(object):
    """A Linked list is initialized with its initial node (a LLnode object)
       whose head is set to 0"""
    def __init__(self,initialNode):
        self.nodeCount=0
        initialNode.head=0
        self.first=initialNode  #the first node in the linked list
        self.last=initialNode   #the last node in the linked list
        
    def addNode(self,newNode):
        """Assumes newNode is an LLnode object"""
        """Attaches the new node to the end of the linked list"""
        self.nodeCount+=1  #Increase the nodeCount. This is the head of the new node
        newNode.head=self.nodeCount
        self.last.nextNode = newNode
        self.last.tail=self.nodeCount  #The last node's tail is the head of the new node
        self.last=newNode  #the new node is now the last node
        
    def findNode(self, value):
        """Assumes node is a value"""
        found = False
        current = self.first
        
        if current.value == value:
            found = True
        else:
            current = current.nextNode
        
        while not found and current != self.last:
            if current.value == value:
                found = True
            else:
                current = current.nextNode
        
        if self.last.value == value:
            found = True
        
        if found:
            return current
        else:
            new = LLnode(value)
            self.addNode(new)              
        
    def __str__(self):
        LL=''
        current = self.first
        LL=LL+str(current.head)+' | '+str(current.value)+' | '+str(current.tail)+'\n'
        
        while current != self.last:
            current = current.nextNode
            LL=LL+str(current.head)+' | '+str(current.value)+' | '+str(current.tail)+'\n'
            
        return LL

#Make some nodes   
a=LLnode('axolotl')
b=LLnode('bear')
c=LLnode('camel')
d=LLnode('dragon')
e=LLnode('elephant')
f=LLnode('frog')

#make a linked list with initial node a
L=LinkedList(a)

#add nodes b,c,d, and e to L
for node in [b,c,d,e,f]:
    L.addNode(node)
   
#print(L)

