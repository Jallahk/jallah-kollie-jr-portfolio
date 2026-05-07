#NearestNeighbor
from math import inf
def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

def nearestNeighbor(new,feature):
    nearest=inf
    value = 0
    for ID in feature:
        old=[float(x) for x in feature[ID][:-1]]
    
        dist=minkowskiDist(new,old,len(old))
    
        if dist < nearest:
            nearest=dist
            value=feature[ID][-1]
            neighbor=ID

    return value,neighbor

