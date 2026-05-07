
from vertex_graph2 import Graph, Vertex
from pythondsBasic import Queue
import copy

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    
    for nbr in currentVert.getConnections():
        
        if (nbr.getColor() == 'white'):
            nbr.setColor('gray')
            nbr.setDistance(currentVert.getDistance() + 1)
            nbr.setPred(currentVert)
            vertQueue.enqueue(nbr)
    currentVert.setColor('black')




'''Jallah Kollie 12-9-25'''

def allPairs(g):
    for i in g.vertList:
        #create a copy of the original graph everytime
        G = copy.deepcopy(g)
        
        # Reset all vertices to white before running BFS
        for n in G.vertList:
            v = G.getVertex(n)
            v.setColor('white')
            v.setDistance(0)
            v.setPred(None)
        
        v1 = G.getVertex(i)
        bfs(G, v1)
        
        for n in G.vertList:  
            v = G.getVertex(n)
            print(f"Distance from {i} to {n}: {v.getDistance()}")
        print()
        
              

    
