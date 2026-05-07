#SidiBel Similarity
import pandas as pd
from math import inf
from NearestNeighbor import *
from scalingFeatures import *

#Get and clean data
sbff = pd.read_csv('SidiBelRegion.csv')
sbff = sbff.drop(['day','year','month'],axis = 'columns')
sbff = sbff.rename(columns ={' RH':'RH',' Ws':'Ws','Rain ':'Rain','Classes  ':'Classes'})
nc = []
for i in sbff['Classes']:
    if 'n' in i:
        nc.append('not fire')
    else:
        nc.append('fire')
sbff['Classes']=nc

#Make feature dictionary
sb ={}
for i in sbff.index:
    sb[i]=list(sbff.loc[i])
    

sbl,scaleFactorsL = linscale(sb)
sbz,scaleFactorsZ = zscale(sb)


new =[32, 71, 12, 0.7, 57.1, 2.5, 8.2, 0.6, 2.8, 0.2]
new2 = [32, 60, 12, 0.7, 57.1, 2.5, 5.2, 0.6, 3.8, 0.2]
newZ = zscaleNew(new,scaleFactorsZ)
newL = linscaleNew(new,scaleFactorsL)

nearestNeighbor(newL,sbl)