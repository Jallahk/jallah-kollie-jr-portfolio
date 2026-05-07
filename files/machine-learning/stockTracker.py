#Stock Tracker

import matplotlib.pyplot as plt

infile = open('stockdata.txt','r')
data = {}
infile.readline()
for line in infile:
    x = line.split('\t')
    date = x[0][:-5]
    if len(date) == 3:
        date = date[0]+date[1]+'0'+date[2]
    
    open_ = float(x[1])
    high =float(x[2])
    low = float(x[3])
    close = float(x[4][:-1])
    
    data[date]=[open_,high,low, close]
    
infile.close()

datelist =[]
closelist =[]
openlist =[]
highlist = []
lowlist = []
for date in data:
    datelist.append(date)
    openlist.append(data[date][0])
    highlist.append(data[date][1])
    lowlist.append(data[date][2])
    closelist.append(data[date][3])

plt.figure()
plt.rcParams['lines.linewidth']=2
plt.rcParams['xtick.labelsize']=6.1
plt.title('StockTracker')
plt.xlabel('2011')
plt.ylabel('Value')

plt.plot(datelist,openlist,color ="red",label='Open')
plt.plot(datelist,highlist,color ="green",label='High')
plt.plot(datelist,lowlist,color ="orange",label='Low')
plt.plot(datelist,closelist,color ="blue",label='Close')

plt.legend(loc='best')  
plt.show()