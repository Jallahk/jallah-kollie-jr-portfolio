#Similarity Based Learning - NFL Draft

import numpy as np
import matplotlib.pyplot as plt
from math import inf

#Here is the feature space of the training data

#takes a data file and turns it into a dictionary
def feature(featureDatafile, splitCh =','):
    infile=open(featureDatafile,'r')
   
    feature={}
    ID=1
    for line in infile:
        feature[ID]=line[:-1].split(splitCh)
        ID+=1
    infile.close()
    return feature


def plotFeatureSpace(feature,new=False):
    plt.rcParams['lines.linewidth']=2
    plt.figure(1)
    plt.title('NFL Draft')
    plt.xlabel('Speed')
    plt.ylabel('Agility')
   
    for ID in feature:
        if feature[ID][2]=='yes':
            plt.plot(float(feature[ID][0]),float(feature[ID][1]),'ro')
        else:
            plt.plot(float(feature[ID][0]),float(feature[ID][1]),'bo')
    
    plt.plot([],'ro',label='Yes')
    plt.plot([],'bo',label='No')
    plt.legend(loc='upper left')
    
    if new:
       plt.plot(new[0],new[1],'gd')
       plt.show()
    else:
        plt.show()


#minkowski metric from Chapter 22

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)


#We'd like to know whether or not to draft a new prospect


new1=[6.75,3.00]
new2=[4.5,3.25]

def nearestNeighborNFL(new,feature):
    nearest=inf
   
    for ID in feature:
        old=[float(x) for x in feature[ID][:-1]]
    
        dist=minkowskiDist(new,old,len(old))
    
        if dist < nearest:
            nearest=dist
            value=feature[ID][-1]
            neighbor=ID
            
    return value,neighbor

file = feature('irisData.txt')

Iris1 = [6.4,2.7,5.7,2.2]
Iris2 = [6.6,3.1,4.6,1.5]
Iris3 = [4.9,3.4,1.6,.06]

for i in[Iris1,Iris2,Iris3]:
    print(nearestNeighborNFL(i,file))        
