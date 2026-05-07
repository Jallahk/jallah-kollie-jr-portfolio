#Derivative Approximation

def  poly(x):
    return x**3 -4*x**2 -3*x +2

def derivative(a, fcn, h):
    return (fcn(a+h) - fcn(a-h))/(2*h)

import matplotlib.pyplot as plt

plt.figure(1)
plt.rcParams['lines.linewidth']=2.0
plt.title('Function and Derivative')
plt.xlabel('x')
plt.ylabel('y')
v=0
h = 0.01
x = []
y = []
y_prime =[]
'''while v <=5:
    y.append(poly(v))
    y_prime.append(derivative(v,poly,h))
    x.append(v)    
    v += h
plt.plot(x,y,color ="blue", label = 'function')
plt.plot(x,y_prime, color = 'red', label = 'derivative')
plt.legend(loc='best')
plt.axhline(y = 0, color = 'black')
plt.axvline(x = 0, color = 'black')
plt.show()'''



infile = open('scidata1.txt','r')
for line in infile:
    ll = line.split()
    x.append(float(ll[0]))
    y.append(float(ll[1]))
infile.close()

yy=[]
for i in range(1,len(x)-1):
    yy.append((y[i+1]-y[i-1])/(x[i+1]-x[i-1]))
xx = x[2:]
    
    
'''plt.plot(x,y,color ="blue", label = 'function')
plt.plot(xx,yy, color = 'red', label = 'derivative')
plt.legend(loc='best')
plt.axhline(y = 0, color = 'black')
plt.axvline(x = 0, color = 'black')
plt.show()'''
    

