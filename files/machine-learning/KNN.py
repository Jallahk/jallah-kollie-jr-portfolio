# -*- coding: utf-8 -*-
"""
KNN 
"""
def feature(featureDatafile, splitCh =','):
    infile=open(featureDatafile,'r')
    
    feature={}
    ID=1
    for line in infile:
        feature[ID]=line[:-1].split(splitCh)
        ID+=1
    infile.close()
    return feature

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

def defineClasses(feature):
    #extract class designations into a list
    classDesignations=[]
    for key in feature:
        if feature[key][-1] not in classDesignations:
            classDesignations.append(feature[key][-1])
    return classDesignations


def KNN(new,f,k):
    neighborList=[]
    count=0
    ID=0
#take the first k entries in the feature dictionary
    while count != k:
        ID +=1
#use only valid IDs    
        if ID in f:
        
            old=[float(v) for v in f[ID][:-1]]
        
            neighborList.append((ID,minkowskiDist(new,old,2)))
            count +=1
#replace farthest item if a closer one is found
    for key in f:
        dist= minkowskiDist(new,[float(v) for v in f[key][:-1]],2)
        currentMax=max(neighborList, key = lambda x: x[1])
        if dist < currentMax[1]:
            neighborList.remove(currentMax)
            neighborList.append((key,dist))
    
#Tally the votes        
    voters=defineClasses(f)
    votes=[]
    for i in range(len(voters)):
        votes.append(0)
   
    for pair in neighborList:
        for i in range(len(voters)):
            if f[pair[0]][len(f[1])-1]==voters[i]:
                votes[i]+=1
       
    most = 0
    decision =['no opinion']
    for i in range(len(votes)):
        if votes[i]>most:
            most = votes[i]
            decision = [voters[i]]
        elif votes[i]==most:
            decision.append(voters[i])
    #print(voters)       
    #print(votes)
    #print(decision)
    return voters,votes,decision


'''print('\nIris:')
f=feature('IrisData.txt')
new = [7.0,4.6,1.4,7.2]
print(KNN(new,f,17))
print('\nNFL:')
g=feature('NFLDraft.txt')
new=[4,5]
print(KNN(new,g,3))
#print('\nRed wine:')
#h=feature('winequality-red.txt',';')
#new = [8.1,0.20,0.4,6.9,0.05,30,88,0.9051,3.26,0.44,10.1]
#print(KNN(new,h,17))'''




