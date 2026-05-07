#CS235 Final Exam 2

#Name:

#No imports are allowed

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
        self.nodeCount=0   #Number of nodes in addition to the initialNode
        initialNode.head=0
        self.first=initialNode  #the first node in the linkedlist
        self.last=initialNode   #the last node in the linked list
        
    def addNode(self,newNode):
        """Assumes newNode is an LLnode object"""
        """Attaches the new node to the end of the linked list"""
        self.nodeCount+=1  #Increase the nodeCount. This is the head of the new node
        newNode.head=self.nodeCount
        self.last.nextNode = newNode
        self.last.tail=self.nodeCount  #The last node's tail is the head of the new node
        self.last=newNode  #the new node is now the last node
        
    def find(self,value):
        """Returns the node in the linked list with the given value."""
        current = self.first
        while current.tail != None:
            if current.value == value:
                return current
            else:
                current = current.nextNode
        if current.value == value:
            return current
    
    def getPrevious(self,node):
        """Returns the node preceding the given node in the Linked List"""
        h = node.head
        current = self.first
        while current != self.last:
            if current.tail == h:
                return current
            current = current.nextNode
        return current
#--------------------------------------------------------------    
    def removeNode(self,value):
        # Find the node to be removed
        node_to_remove = self.find(value)
    
        # If the node is the first node
        if node_to_remove == self.first:
            self.first = node_to_remove.nextNode
            self.first.head = 0
        else:
        # Find the node before the one to be removed
            prev = self.getPrevious(node_to_remove)
            prev.nextNode = node_to_remove.nextNode
            if node_to_remove.nextNode:  
                prev.tail = node_to_remove.head
                node_to_remove.nextNode.head = prev.tail
            else:  # Removing the last node
                prev.tail = None
                self.last = prev

        self.nodeCount -= 1
        
        
   
        
 
#-------------------------------------------------------------   
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
    
print(L)