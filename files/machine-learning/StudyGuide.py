from NearestNeighbor import *
from scalingFeature import *
from evaluatingClassifiers import *
from random import seed,randint


infile = open('irisData2.txt', 'r')

irs = {}
index = 0
for line in infile:
    ll = line[:-1].split(',')
    irs[index] = ll
    index += 1

infile.close()


seed(10)

test = []
rmlist = []

while len(test) < 20:
    n = randint(0, len(irs.keys()))
    
    if n not in rmlist:
        rmlist.append(n)
        test.append(irs[n])

for i in test:
   
   print(i[-1], nearestNeighbor([float(x) for x in i[:-1]],irs))
   



