import matplotlib.pyplot as plt
from math import sin

plt.figure()
plt.rcParams['lines.linewidth']=0.5
plt.title('Graphy Thingy')
plt.xlabel('X')
plt.ylabel('Y')

x=[]
y=[]
for i in range(50):
    x=x+[i]
    j=i*2/7
    y=y+[j]

x2,y2=[],[]
for i in range(50):
    x2=x2+[i]
    j=-i*2/7
    y2=y2+[j]


x3,y3=[],[]
for i in range(50):
    x3=x3+[i]
    j=sin(i)
    y3=y3+[j]
    
#plot (x,y) pairs from x, y lists
plt.plot(x,y,color ="blue",label='Up') 
plt.plot(x2,y2,"red",marker='^',label='Down') 
plt.plot(x3,y3,'green', marker = 'o', label = 'Up-Down')

plt.legend(loc='best')  
plt.show()
plt.savefig('silly.png')





