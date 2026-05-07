"""
Birmingham Car Park Stats
E. Hazard
February 30,2020
"""
from math import inf
infile = open('parking.txt', 'r')

# A dictionary of records keyed by car park name
parkDict = {}  

# A dictionary of capacities keyed by car park name
parkCap = {}

# A list of car park names
carparks = []  
 
for line in infile:
    
    dataList = line[:-1].split('\t')
    
  
    if dataList[0] not in parkDict:
        
        
        parkCap[dataList[0]] = float(dataList[1])
        parkDict[dataList[0]] = [dataList[2:]]
        carparks.append(dataList[0])     
        
    else:
        parkDict[dataList[0]].append(dataList[2:])

infile.close()

outfile = open('Birminghamtab.txt','w')
#Find the maximum/minimum occupancy of a specified car park
print('Maximum and minimum occupancy',file = outfile)
def maxminOcc(carpark):
    maxOcc= 0
    minOcc = inf
    maxDateTime = ''
    minDateTime = ''
    for record in parkDict[carpark]:
        if int(record[0] ) > maxOcc:
            maxOcc=int(record[0])
            maxDateTime=record[1]
            
        elif int(record[0]) < minOcc:
            minOcc=int(record[0])
            minDateTime=record[1]
            
    return [(maxOcc,maxDateTime),(minOcc,minDateTime)]

carparkOcc ={}
for carpark in carparks:
    Occ = maxminOcc(carpark)
    print(carpark, Occ,file = outfile)
    carparkOcc[carpark] = Occ

print('Average Occupancy Rate',file = outfile)
avgOccRate ={}
for carpark in carparks:
    total = 0
    count = 0
    for entry in parkDict[carpark]:
        total = int(entry[0]) + total
        count +=1
    avgOccRate[carpark] = (total/count)/parkCap[carpark]*100
    print('{0}: {1:0.2f}%'.format(carpark,avgOccRate[carpark]),file = outfile)

outfile.close()




