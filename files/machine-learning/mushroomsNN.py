#Mushrooms
from NearestNeighbor import *
from scalingFeature import *
#Feature dictionary
infile = open('mr.txt','r')
mr ={}
index = 0
for line in infile:
    linelist = line[:-1].split(',')
    mr[index]=[ord(c) for c in linelist[1:]]+[linelist[0]]
    index+=1
infile.close()

infile = open('unknown.txt','r')
unk =[]
for line in infile:
    linelist = line[:-1].split(',')
    unk.append([ord(a) for a in linelist])
infile.close()

for u in unk:
    print(nearestNeighbor(u,mr))

mrZ,sfZ = zscale(mr)
testZ=[]
for t in unk:
    tz = zscaleNew(t[:-1], sfZ)
    tz.append(t[-1])
    testZ.append(tz)
print()

for t in testZ:
    print(nearestNeighbor(t[:-1],mrZ))

mrL,sfL = linscale(mr)
testL = []
for t in unk:
    tz = linscaleNew(t[:-1], sfL)
    tz.append(t[-1])
    testL.append(tz)
print()
for t in testL:
    print(nearestNeighbor(t[:-1],mrL))


TP,FP,TN,FN = 0,0,0,0

for u in unk:
    pred = (nearestNeighbor(u,mr))
    act = mr[-1]
    if act == 'e':
        if pred[0] == 'e':
            TP +=1
        if pred[0] == 'p':
            FP +=1
    if act == 'p':
        if pred[0] == 'p':
            TN +=1
        if pred[0] == 'e':
            FN +=1
    
    
from evaluatingClassifiers import *

get_stats(TP,FP,TN,FN)    



