import matplotlib.pyplot as plt

infile=open('mysteryFunction.txt','r')
x,y=[],[]
for record in infile:
    
    xstr,ystr = record.split(',')
    xval = float(xstr)
    yval=float(ystr)
    x.append(xval) 
    y.append(yval)
infile.close()
    
plt.figure(1)
plt.rcParams['lines.linewidth']=2.0
plt.title('Mystery Graph')
plt.xlabel('x')
plt.ylabel('y')




    
#plot (x,y) pairs from x, y lists
plt.plot(x,y,color ="blue",label='Mystery Function') 

plt.legend(loc='best')  
plt.show()
plt.savefig('mysteryGraph')


