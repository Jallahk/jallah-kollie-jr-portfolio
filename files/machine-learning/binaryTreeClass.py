from DigraphClass import *

class BTNode(Node):
    """A BTNode has a name and a numerical value. It is created with its value."""
    def __init__(self, value = None):
        
        if value == None:   #The None node is special
            self._name = 'None'
        else:    
            self._name = str(value)
        self._value = value
        
    def get_value(self):
        return self._value
    
class BT(Digraph):  #Binary Tree Class
    """Binary trees are rooted trees in which each node has at most 2 children"""
    
    none = BTNode()   #The none node is a class attribute
    
    def __init__(self,root):
       """Assumes that root is a BTNode"""
       self.root = root
       self._nodes = [root]
       self._edges = {root:[BT.none,BT.none],BT.none:[]}
       
       
    def add_child(self,parent,LR,child):
        """Assumes parent and child are BTNodes"""
        if LR not in ['left','right']:
            raise ValueError("'{0}' is not 'left' or 'right'".format(LR))
        if child in self._nodes:
           raise ValueError('Duplicate node')
        else:
            self._nodes.append(child)
            self._edges[child]=[BT.none,BT.none]
            if LR == 'left':
                if self._edges[parent][0] != BT.none:
                   raise ValueError('Left child already present') 
                self._edges[parent][0] = child
            else:
                if self._edges[parent][1] != BT.none:
                   raise ValueError('Right child already present')  
                self._edges[parent][1] = child
      
    def get_left_child(self,node):
        
        return self._edges[node][0]
    
    def get_right_child(self,node):
        
        return self._edges[node][1]
    
    def get_node_from_value(self,value):
         
        name = str(value)
        return self.get_node_from_name(name)
    
    def get_parant_of(self,node):
        ''''returns the parant node'''
        for pp in self._edges:
            if node in self._edges:
                 return pp
            
    def binary_to_path(self,binaryString):
        '''
        binary string that represent the path to take
        returns the path the string represent'''
        
        curNode = self.root
        pathString = '{0}'.format(curNode.get_name())
        
        for route in binaryString:
            if route == '0':
                
                left_Node = self._edges[curNode][0]
                if left_Node == BT.none:
                    return pathString
                
                else:
                    pathString += '->{0}'.format(left_Node.get_name())
                    
                    curNode = left_Node
                
                
            
            elif route == '1':
                
                right_Node = self._edges[curNode][1]
                if right_Node == BT.none:
                    return pathString
                
                else:
                    pathString += '->{0}'.format(right_Node.get_name())
                    
                    curNode = right_Node
                
            else:
                raise ValueError('Not a Binary String')
            
            
        return pathString
    
    
bt = BT(BTNode(8))
new1 = BTNode(11)
new2 = BTNode(9)
new3 = BTNode(2)
new4 = BTNode(5)
bt.add_child(bt.root,'right',new1)
bt.add_child(new1,'left',new2)
bt.add_child(bt.root,'left',new3)
bt.add_child(new3,'right',new4)

print(bt.binary_to_path('01'))



bt = BT(56)
def make_bst(bst,lis):

    for node in lis:
        placed = False
        current_node = bst.root
        while not placed:
            if node >= current_node.get_value():#go right
                next_node = bst.getright_child(current_node)
                if next_node == BT.none: #empty spot located
                    bst.add_child(current_node, 'right', BTNode(node))
                    placed = True #breaks out of the while loop
                    
                else:
                    current_node = next_node #keep looking
            elif node < current_node.get_value(): #go left
                next_node = bst.get_left_child(current_node)
                if next_node == BT.none: #empty spot located
                    bst.add_child(current_node,'left', BTNode(node))
                    placed = True #breaks the while loop
                    
                else:
                    current_node = next_node #keep looking
               
                
def addNode(tree, val:int):
    
    for num in tree:
        current_node = tree.root
    
        placed = False
    
        while not placed:
            if val >= current_node.get_value():
                next_node = tree.getright_child(current_node)
                if next_node == BT.none
                    tree.add_child(val,'right',BTNode(num))
                    
                else:
                    current_node = next_node
                    
            elif val < current_node.get_value():
                next_node = tree.getleft_child(current_node)
                if next_node == BT.none:
                    tree.add_child(val,'left',BTNode(num))
                    placed = True
                    
                else:
                    current_node = next_node
                
        
            
    