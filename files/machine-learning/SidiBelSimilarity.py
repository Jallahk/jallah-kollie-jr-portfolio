#SidiBel Similarity
import pandas as pd
from math import inf
from NearestNeighbor import *
from scaling import *

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
    
#Linear scaling: Linearly scales all the data
scaleFactors = []
for col in range(len(sb[0])-1):
    templist = []
    for i in sbff.index:
        templist.append(sb[i][col])
    templist,vmin,vmax = linear_scale(templist)
    scaleFactors.append([vmin,vmax-vmin])
    for i in sbff.index:
        sb[i][col]=templist[i]

#Use this function to scale new data based upon old data       
def scaleNew(new, scaleFactors):
    for i in range(len(new)):
        new[i] = (new[i]-scaleFactors[i][0])/(scaleFactors[i][1])
    return new

new =[32, 71, 12, 0.7, 57.1, 2.5, 8.2, 0.6, 2.8, 0.2]



