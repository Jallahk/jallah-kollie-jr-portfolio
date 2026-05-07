#Buffon in 3-D
from random import random
def minkowski(p1,p2,n):
    #Assume p1 and p2 are n-tuples representing coordinates in Euclidan n-space
    total = 0
    for i in range(n):
        total += (p1[i]-p2[i])**2
    return total**(1/n)

def throw_needles(num_needles):
    in_circle = 0
    for Needles in range(1, num_needles + 1):
        x = random()
        y = random()
        z = random()
        if minkowski((x,y,z),(0,0,0),3) <= 1:
            in_circle += 1
    #Counting needles in one quadrant only, so multiply by 4
            
    return 6*(in_circle/num_needles)