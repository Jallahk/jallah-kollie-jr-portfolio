import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics

est = LinearRegression(fit_intercept = True)
advfile = open('advertising.txt','r')
headings = advfile.readline().split()
x=[]
y=[]
for line in advfile:
   lineList = line.split()
   x.append([float(v) for v in lineList[:-1]])
   y.append(float(lineList[-1]))
advfile.close()
est.fit(x,y)

print(est.coef_,est.intercept_)




y_hat = est.predict(x)
print('Coefficient of Determination:',metrics.r2_score(y,y_hat))
    




