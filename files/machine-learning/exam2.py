#CS235 Exam #2
#Name: Jallah Kollie

from evaluatingClassifiers import *
from NearestNeighbor import *
from scalingFeature import *

rd ={} #Feature Dictionary
idnum = 0
infile = open('Raisin_Data.txt','r')
for line in infile:
    linelist = line[:-1].split()
    rd[idnum] = [float(x) for x in linelist[:-1]]+[linelist[-1]]
    idnum+=1
infile.close()

testRaisins = [] #List of test raisins
infile = open('raisinTestdata.txt','r')
for line in infile:
    linelist = line[:-1].split()
    test = [float(x) for x in linelist[:-1]]+[linelist[-1]]
    testRaisins.append(test)
infile.close()

#Zscale the data in rd and testraisins
rdz,scalefactz = zscale(rd)

TP,FP,TN,FN = 0,0,0,0
for Zlis in testRaisins:
    Tlistz =zscaleNew(Zlis[:-1],scalefactz) 
    #apply nearestNeighbor
    pred = nearestNeighbor(Tlistz,rdz)
  
    act = Zlis[-1]
    if act == 'Besni':
        if pred[0] == 'Besni':
            TP +=1
        if pred[0] == 'Kecimen':
            FN +=1
    if act == 'Kecimen':
        if pred[0] == 'Kecimen':
            TN +=1
        if pred[0]=='Besni':
            FP +=1
        
    
   
    
#Classification     
    
get_stats(TP,FP,TN,FN)
    

#confusion matrix
print("\nConfusion Matrix:")
print("               Predicted")
print("             | Besni | Kecimen")
print("Actual ------|-------|--------")
print(f"  Besni      |  {TP:5} |  {FN:7}")
print(f"  Kecimen    |  {FP:5} |  {TN:7}")
