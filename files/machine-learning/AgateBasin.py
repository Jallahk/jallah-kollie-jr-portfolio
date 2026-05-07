# -*- coding: utf-8 -*-
"""
K-means on Agate Basin Projectile Points
"""
from ClusterCounts import *


#attribute 8
rockDict ={'Chert':1, 'Quartz':2, 'KRF':3}
#attribute 7
baseDict ={'Round':1,'Straight':2,'Concave':3,'Crushed':4}
#attribute 6
marginsDict= {'Curved':1, 'Straight':2}

agateEx =[]
infile = open('projectile_points_Agate_Basin.txt','r')
for line in infile:
    if line != 'EOF':
        lineList = line[:-1].split(',')
        name = lineList[0]
        features = lineList[1:]
        features2=[]
        for i in range(9):
            if i == 8:
                features2.append(rockDict[features[i]])
            elif i==7:
                 features2.append(baseDict[features[i]])  
            elif i == 6:
                features2.append(marginsDict[features[i]])
            else:
                features2.append(float(features[i]))
        agateEx.append(Example(name,features2))    
        
infile.close()

best = trykmeans(agateEx,3,300)

for cluster in best:
    print(cluster.__str__())
    #print(cluster.variability())

#print('\n',dissimilarity(best))




