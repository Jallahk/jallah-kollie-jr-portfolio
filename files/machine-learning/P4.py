'''Jallah Kollie program 4- Wine Quality, 3-28-2025'''
import pandas as pd
from math import inf
from NearestNeighbor import *
from scalingFeatures import *
from random import choice,seed

#reads the file 
rw = pd.read_csv('winequality-red.csv', sep = ';')

#removes 5 randomly selected instances from the file
seed(15)
lst = [a for a in range(1598)]
rmlist = []
for i in range(5):
    k = choice(lst)
    lst.remove(k)
    rmlist.append(k)

test = []
for k in rmlist:
    test.append(list(rw.loc[k]))
    
rw = rw.drop(rmlist)

x = pd.RangeIndex(len(rw.index))

rw.index = range(len(x))

#create feature dictionary 
fd = {}
for i in rw.index:
    fd[i] = list(rw.loc[i])
    

#classifys the removed instances without scaling
#predictions = []


for lis in test:
    prediction = (nearestNeighbor(lis[:-1],fd))
    print(lis[-1],prediction)
    


print()


    
#classify with linear scale and zscale    
rwl,scalefactL = linscale(fd)
rwz,scalefactz = zscale(fd)

#linear Scale
for Linlis in test:
    TlistL = linscaleNew(Linlis[:-1],scalefactL)
    prediction2 = nearestNeighbor(TlistL,rwl)
    
    print(Linlis[-1], prediction2)
    
print()

#zscale 
for Zlis in test:
    Tlistz = linscaleNew(Zlis[:-1],scalefactz)
    prediction3 = nearestNeighbor(Tlistz,rwz)
    
    print(Zlis[-1], prediction3)
    

'''without scaling my program made two errors, with the third row being off by one which is not too bad of an error
and the 4th row being off by 2 which is a more significant error than the other, which could mean there is
probably a different wine that it is closest to.'''
    
'''as for the scaling, the Zscale did a better job than the linscale with the zscale only producing one error,
    which was only off by one'''








