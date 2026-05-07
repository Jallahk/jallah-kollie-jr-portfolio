#dealing with qualitative data
import pandas as pd


#1

congr = {}

idnum = 1

file = open('voting.txt','r')

for line in file:
    linelist = line[:-1].split(',')
    congr[idnum] = linelist
    idnum+=1
    
file.close()

#2
def quant(val):
    if val == 'y':
        return 1
    elif val == '?':
        return 0
    else:
        return -1
    
cvrn = {}
for k in congr:
    cvrn[k] = [quant(val) for val in congr[k][:-1]]
    cvrn[k].append(congr[k][-1])
    
#3
from random import randint,seed
seed(0)
rmlist = []
testRecords = []
while len(rmlist) <30:
    m = randint(1,435)
    if m not in rmlist:
        rmlist.append(m)
        testRecords.append(cvrn[m])
        del cvrn[m]