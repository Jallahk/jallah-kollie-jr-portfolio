from NodeClass import Node

class LinkedList:
    def __init__(self):
        self.head = None #the head is the first item in the list
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item): #add to front of list
        temp = Node(item)      #turn item into a Node
        temp.setNext(self.head)  #new node points to old head of list
        self.head = temp #new head of list
        
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext() #visit every node 
        return count
    
    def search(self,item): #O(n)
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self,item):
        current = self.head
        while current.getNext() != None: 
            current.getNext()
        current.setNext(Node(item))
            

   # def index(self,iten):

    #def pop(self,item):




#Example

x=LinkedList()
for i in [14,23,11,6,19,8,10]:
    x.add(i)

x.remove(23)
x.append(5)
print(x.length())
#print(x.search(11))

print(x.length())

