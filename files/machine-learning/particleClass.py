import numpy as np
import random

class Particle():
    """Particles are defined by the dimension of the space in which they fly"""
    
    def __init__(self, dim):
        self.pos = np.array([0.0]*dim)
        self.vel = np.array([0.0]*dim)
        self.dim = dim
        self.best = np.array([0.0]*dim)
        
    def initialPos(self, bound, firstQuad = True):
        """A particle's initial position is assigned randomly in (0,bound)
        if the position should be in (-bound,bound) then set firstQuad = False"""
        if firstQuad:
            for i in range(self.dim):
                self.pos[i]= bound*random()
        else:
            for i in range(self.dim):
                self.pos[i]= 2*bound*random()-bound
    
    def updateBest(self, obj):
        """obj is an objective function"""
        if obj(self.pos) < obj(self.best):
            self.best = self.pos
            
            
            
            