#Bidirectional Associative Memory (BAM)
from MatrixClass import *
class BAM:
    
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.weights = Matrix(n,m)
    
    def calcWeights(self,patt):
        
        for p in patt:
            self.weights += p[0]*p[1].transpose()
    
    def associatexy(self,x):
        return (self.weights.transpose()*x).sign()
    
    def associateyx(self,y):
        return (self.weights*y).sign()
    
        
            
 


#Making the pattern in matrices
p2 = [[[1,1],[1,-1,1]],[[-1,-1],[-1,1,-1]]]



def pat2mat(pat,n,m):
    """Converts a pattern of lists into a pattern of matrices for BAM"""
    p2M =[]
    for p in pat:
        xx = Matrix(n,1)
        xx.mat = [[a] for a in p[0]]
        yy = Matrix(m,1)
        yy.mat = [[a] for a in p[1]]
        p2M.append([xx,yy])
    return p2M

def list2mat(lst):
    lm = Matrix(len(lst),1)
    lm.mat = [[a] for a in lst]
    return lm

p2M = pat2mat(p2,2,3)
q=BAM(2,3)
q.calcWeights(p2M)
print(q.associateyx(p2M[0][1]))
print(q.associatexy(p2M[1][0]))

p3 = [[[1,1,1],[1,1,1,1]],[[1,-1,1],[1,-1,-1,1]],[[1,1,-1],[1,1,-1,-1]],[[-1,1,1],[-1,-1,1,1]]]
p3M = pat2mat(p3,3,4)
q1 = BAM(3,4)
q1.calcWeights(p3M)

ex =[1,-1,-1]
exM = list2mat(ex)
print(exM)
print(q1.associatexy(exM))


