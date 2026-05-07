import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics

est = LinearRegression(fit_intercept = True)
advfile = open('advertising TV.txt','r')
headings = advfile.readline().split()
x=[]
y=[]
for line in advfile:
    x.append([float(line.split()[0])])
    y.append(float(line.split()[1]))
advfile.close()
est.fit(x,y)

print(est.coef_,est.intercept_)
y_hat = est.predict(x)
print('Coefficient of Determination:',metrics.r2_score(y,y_hat))

def regrline(coef,intc,x):
    return coef*x + intc

plt.figure('Advertising Data')
plt.rcParams['lines.linewidth']=0.5
plt.title('Sales from TV Advertising')
plt.xlabel('Budget')
plt.ylabel('Sales Units')

for i in range(200):
    plt.plot(x[i],y[i],marker ='.',color = 'blue')
    
line =[]
for v in x:
    line.append(regrline(est.coef_,est.intercept_,v[0]))
plt.plot(x,line,color ='red')
plt.show()


    
advfile = open('advertising radio.txt','r')
headings = advfile.readline().split()
x=[]
y=[]
for line in advfile:
    x.append([float(line.split()[0])])
    y.append(float(line.split()[1]))
advfile.close()
est.fit(x,y)

print(est.coef_,est.intercept_)
y_hat = est.predict(x)
print('Coefficient of Determination:',metrics.r2_score(y,y_hat))

def regrline(coef,intc,x):
    return coef*x + intc

plt.figure('Advertising Data')
plt.rcParams['lines.linewidth']=0.5
plt.title('Sales from Radio Advertising')
plt.xlabel('Budget')
plt.ylabel('Sales Units')

for i in range(200):
    plt.plot(x[i],y[i],marker ='.',color = 'blue')
    
line =[]
for v in x:
    line.append(regrline(est.coef_,est.intercept_,v[0]))
plt.plot(x,line,color ='red')
plt.show()



advfile = open('advertising newspaper.txt','r')
headings = advfile.readline().split()
x=[]
y=[]
for line in advfile:
    x.append([float(line.split()[0])])
    y.append(float(line.split()[1]))
advfile.close()
est.fit(x,y)

print(est.coef_,est.intercept_)
y_hat = est.predict(x)
print('Coefficient of Determination:',metrics.r2_score(y,y_hat))

def regrline(coef,intc,x):
    return coef*x + intc

plt.figure('Advertising Data')
plt.rcParams['lines.linewidth']=0.5
plt.title('Sales from Newspaper Advertising')
plt.xlabel('Budget')
plt.ylabel('Sales Units')

for i in range(200):
    plt.plot(x[i],y[i],marker ='.',color = 'blue')
    
line =[]
for v in x:
    line.append(regrline(est.coef_,est.intercept_,v[0]))
plt.plot(x,line,color ='red')
plt.show()


    




