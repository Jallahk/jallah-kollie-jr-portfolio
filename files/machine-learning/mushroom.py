import pandas as pd
from NearestNeighbor import *
from scalingFeatures import *



mr = open('mr.txt','r')

mrd = {}
idnum = 0
for line in mr:
    ll = line[:-1].split(',')
   
    mrd[idnum] = ll[1:] + [ll[0]]
    idnum +=1
     
    
mr.close()


for k in mrd.keys():
    
    qf = [ord(x) for x in mrd[k][:-1]]
    clas = mrd[k][-1]
    mrd[k] = qf+[clas]
    
mrl,scalefactL = linscale(mrd)
mrz,scalefactz = zscale(mrd)
        

unk = open('unknown.txt','r')

for line in unk:
    nll = line[:-1].split(',')
    

    
unk.close()
   
        
