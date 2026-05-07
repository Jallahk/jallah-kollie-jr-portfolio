#Finding extrema


def derivative(a, fcn, h):
    return (fcn(a+h) - fcn(a-h))/(2*h)

def Extrema(f,a,b):
    locmin =[]
    locmax =[]
    x = a
    while x <= b:
        d1 = derivative(x,f,.001)
        d2 = derivative(x+.001,f,.001)
        if d1*d2 < 0:
            if d1 > 0:
                locmax.append(x+.0005)
            else:
                locmin.append(x+.0005)
        x +=.001
    x=a
    globmin = f(x)
    for x in locmin + [b]:
        if f(x) < globmin:
            globmin = f(x)
            gminx = x
    x=a
    globmax = f(x)
    for x in locmax + [b]:
        if f(x) > globmax:
            globmax = f(x)
            gmaxx = x        
    
    
    
    return locmin,locmax,globmin,gminx,globmax,gmaxx

from math import sin,cos
def g(x):
    return 2*cos(x-4)+3*(x-5)*sin((x-5)/2)

locmin,locmax,globmin,gminx,globmax,gmaxx = Extrema(g,0,10)

print('Local minima at x in',[round(x,3) for x in locmin])
print('Local maxima at x in',[round(x,3) for x in locmax])
print('Global max is {0:0.3f} at x = {1:0.3f}'.format(globmax,gmaxx))
print('Global min is {0:0.3f} at x = {1:0.3f}'.format(globmin,gminx))

