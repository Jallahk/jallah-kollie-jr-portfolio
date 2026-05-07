#Barrel Question
from random import *

#make the barrel and it's contents.

barrel =[]
for i in range(10000):
    barrel.append('r')
    
for i in range(8000):
    barrel.append('b')
    
for i in range(6000):
    barrel.append('y')
    
    
shuffle(barrel) #mix up the barrel

#procedure Z

def z(barrel):
    m = choice(barrel)
    
    if m == 'b':
        barrel.remove(m)
        barrel.append('y')
        
    elif m == 'y':
        barrel.remove(m)
        barrel.append('r')
        
    else:
        barrel.remove(m)
        barrel.append('b')
    
    shuffle(barrel)
    
    return barrel


for i in range(8000):
    barrel = z(barrel)
    
probDict = {}
for m in 'rby':
    probDict[m] = barrel.count(m)/24000
print(probDict)
    