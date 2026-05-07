#Wine quality regression
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
est = LinearRegression(fit_intercept = True)
winefile = open('winequality-red.txt','r')

x=[]
y=[]
for line in winefile:
    lineList = line[:-1].split(';')
    x.append([float(v) for v in lineList[:-1]])
    y.append(float(lineList[-1]))
winefile.close()
est.fit(x,y)

print(est.coef_,est.intercept_)
def regrline(coef,intc,x):
    prod = 0
    for i in range(len(coef)):
        prod += coef[i] * x[i]
    return prod + intc
    

print(round(regrline(est.coef_,est.intercept_,x[0])),0)

y=np.array(y)
y_hat = est.predict(x)

