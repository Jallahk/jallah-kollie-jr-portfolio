'''Jallah Kollie, Program 7, May 2,2025'''

from naiveBayes import *
from KNN import *
from NearestNeighbor import *
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics


#1

#create feature dictionary
fd ={} #Feature Dictionary
idnum = 0
infile = open('lymphTrain.txt','r')
for line in infile:
    linelist = line[:-1].split(',')
    fd[idnum] = [int(x) for x in linelist]
    idnum+=1
infile.close()

#appends all the data in lymphTrain to a list
div = 0
infile = open('lymphTest.txt','r')
classi = []
new =[]
for line in infile:
    ll = line[:-1].split(',')
    llis = [int(x) for x in ll[:-1]]
    classi.append(int(ll[-1]))
    new.append(llis)
    div+=1


infile.close()
#making my predictios
Bperc = 0
Kperc = 0
Nperc = 0

for index,lis in enumerate(new):
  
   bay = Bayes(lis,fd)
   #print(bay)
   
   if bay[-1]==classi[index]:
       Bperc+=1
        
   
   
   
   NN = nearestNeighbor(lis,fd)
   #print(NN)
   
   
   if NN[0] == classi[index]:
       Nperc+=1
   
   kn = KNN(lis,fd,3)
   #print(kn)
   
   if kn[-1][-1] == classi[index]:
       Kperc+=1
  
       
Kacc = round(Kperc/div*100,1)
Bacc = round(Bperc/div*100,1)
Nacc = round(Nperc/div*100,1)

#print(Kacc,Bacc,Nacc)

#multilinear regression
   
est = LinearRegression(fit_intercept = True)
advfile = open('lymphTrain.txt','r')
headings = advfile.readline().split()
x=[]
y=[]
for line in advfile:
   ll = line.split(',')
   llis = [int(x) for x in ll]
   x.append([float(v) for v in llis[:-1]])
   y.append(float(llis[-1]))
advfile.close()
est.fit(x,y)

#print(est.coef_,est.intercept_)

Mperc = 0

infile = open('lymphTest.txt','r')

for line in infile:
    tot = 0
    mll = line[:-1].split(',')
    mllis = [int(x) for x in mll[:-1]]
    
    for i in range(len(mllis)):
        mult = est.coef_[i]*mllis[i]
        tot+=mult
    
    tot+=est.intercept_
    
    if round(tot,0) == int(mll[-1]):
        Mperc+=1

    #print(int(tot))

infile.close()

Macc = round(Mperc/div*100,1)


#print(Macc)

#prints my output

print(f'The naive Bayes classifier correctly classified {Bacc}% of the test data')    

print(f'The nearest neighbor algorithm correctly classified {Nacc}% of the test data')

print(f'The KNN algorithm (k=3) correctly classified {Kacc}% of the test data')

print(f'The multilinear regression algorithm correctly classified {Macc}% of the test data')       
   
   
   