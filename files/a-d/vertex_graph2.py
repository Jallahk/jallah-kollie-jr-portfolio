"""
Graph and Vertex Classes
"""
import sys
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = sys.maxsize
        self.pred = None
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.distance = d

    def setPred(self,p):
        self.pred = p

    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.distance
        
    def getColor(self):
        return self.color
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    def __str__(self):
        return str(self.id) + ' connectedTo: '\
               + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
             self.addVertex(f)
        if t not in self.vertList:
             self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],
                                         cost)
    
    def getVertices(self):
        return self.vertList.keys()
        
    def __iter__(self):
        return iter(self.vertList.values())

g=Graph()

edges=[(1,2,4),(1,3,2.1),(3,4,5.6),(2,5,1),(2,4,3),(1,5,3.2)]
for e in edges:
    g.addEdge(e[0],e[1],e[2])
    
    
   
    
