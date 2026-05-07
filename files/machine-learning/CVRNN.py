#Nearest Neighbor with Qualitative Attributes

#Congressional Voting Records Data
from NearestNeighbor import *
from scalingFeatures import *

#Make the feature dictionary
cvr ={}
infile = open('voting.txt','r')
index = 0
for line in infile:
    lineList = line[:-1].split(',')
    cvr[index]=lineList
    index+=1
infile.close()

#Quantify data

for k in cvr.keys():
    quant = []
    for item in cvr[k]:
        if item =='y':
            quant.append(1)
        elif item == 'n':
            quant.append(-1)
        elif item == '?':
            quant.append(0)
        else:
            quant.append(item)
    cvr[k]=quant


#Now get training and test sets.
#I'll work directly with the feature dictionary
from random import choice,seed, randint
seed(10)
test =[]
rmlist =[]
while len(test) < 30:
    n = randint(0,len(cvr.keys()))
    if n not in rmlist:
        rmlist.append(n)
        test.append(cvr[n])

cvrTrain = {}
idnum = 0
for k in cvr.keys():
    if k not in rmlist:
        cvrTrain[idnum] = cvr[k].copy()
        idnum +=1

        
#cvrZ,sf = zscale(cvrTrain)

    



TP,FP,TN,FN = 0,0,0,0

for t in test:  #democrat is positive
    pred = nearestNeighbor(t[:-1],cvrTrain)
    act = t[-1]
    if act == 'democrat':
        if pred[0] == 'democrat':
            TP +=1
        if pred[0] == 'republican':
            FN +=1
    if act == 'republican':
        if pred[0] == 'republican':
            TN +=1
        if pred[0]=='democrat':
            FP +=1
            
from evaluatingClassifiers import *

get_stats(TP,FP,TN,FN)
      



