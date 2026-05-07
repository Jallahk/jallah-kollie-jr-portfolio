import numpy as np


x=[]
y=[]
infile = open('curve5.txt','r')
for line in infile:
    data = line.split()
    x.append(float(data[0]))
    y.append(float(data[1]))
infile.close()

import math
#logy = [math.log(a,2) for a in y]
#y=logy.copy()
c = np.polyfit(x, y,4)
p = np.poly1d(c)

import matplotlib.pyplot as plt
plt.scatter(x, y, label='Data')

plt.plot(x, p(x), label='Fitted Polynomial', color='red')

plt.legend()
plt.show()

ymean = np.mean(y)
ss_total = np.sum((y - ymean)**2)
ss_res = np.sum((y - p(x))**2)
r_squared = 1 - (ss_res / ss_total)

print(r_squared)