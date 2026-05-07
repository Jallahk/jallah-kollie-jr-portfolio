def derivative(a,fcn,h):
    return(fcn(a+h) - fcn(a-h))/(2*h)

#Newton's Method

def Newton(fcn,guess,epsilon,h):
    """finds a root of fcn near guess using deravative approx"""
    while abs(fcn(guess))> epsilon:
        new = guess - fcn(guess)/derivative(guess,fcn,h)
        guess = new
    return guess


def f1(x):
    return x**2 -4

from math import sin,cos,log, e

def f2(x):
    return cos(x + 2*log((abs(2*x)+0.02),10)) - 3*x/40*sin(x)*log(x**2+1,e)

x = .5
posroot = []
while x < 4:
    y1 = nasty(x)
    y2 = nasty(x+.5)
    if y1*y2 < 0:
        posroot.append(x+.1)
    x = x+.1
        