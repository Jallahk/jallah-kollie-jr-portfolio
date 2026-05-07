from ClusterCounts import *
import matplotlib.pyplot as plt

infile=open('NFLDraft.txt','r')
    
data={}
ID=1
for line in infile:
    data[ID]=line[:-1].split(',')
    ID+=1
infile.close()
    
data1 ={}
for k in data:
    data1[k]=[float(x) for x in data[k][:-1]]+[data[k][-1]]

exNFL =makeExamples(data1)

q=kmeans(exNFL,2)
for b in q:
    print(b)
"""    
best = trykmeans(exNFL,2,100)
for b in best:
    print(b)
"""
def plotData(data,new=False):
    plt.rcParams['lines.linewidth']=2
    plt.figure(1)
    plt.title('NFL Draft')
    plt.xlabel('Speed')
    plt.ylabel('Agility')
   
    for ID in data:
        if data[ID][2]=='yes':
            plt.plot(float(data[ID][0]),float(data[ID][1]),'ro')
        else:
            plt.plot(float(data[ID][0]),float(data[ID][1]),'bo')
        plt.text(float(data[ID][0]),float(data[ID][1]),'  '+str(ID))
    plt.plot([],'ro', label='Yes')
    plt.plot([],'bo',label='No')
    plt.legend(loc='upper left')
    
    if new:
       plt.plot(new[0],new[1],'gd')
       plt.plot([],'gd',label='?')
       plt.legend(loc='upper left')
       plt.show()
    else:
        plt.show()


plotData(data)
#new1=[6.75,6.00]
#plotData(data,new1)

