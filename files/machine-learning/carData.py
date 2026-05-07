#car data

cfd ={}
idnum = 0
infile = open('car2.txt','r')
for line in infile:
    LL = line[:-1].split(',')
    cfd[idnum]=LL
    idnum +=1
infile.close()

newcar = ['med','low','2','more','big','high']




    

