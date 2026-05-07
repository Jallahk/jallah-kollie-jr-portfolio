infile = open('parking.txt','r')
infile.readline()
lot =[]
sev = []
num = []
date = []
time = []
for line in infile:
    line.split(' ')
    lot, sev,num, date = line.split('\t')
    print(lot)
    
for i in num:
    if i > 