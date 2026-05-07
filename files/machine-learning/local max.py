from derivative import *
from math import cos,sin

def f(x):
    return 2*cos(x-4)+3*(x-5)*sin((x-5)/2)


def Extrema(f,a,b):
    s = a
    g = b
    h =0.01
    local_min = []
    local_max = []
    
    while s <= g:
        ans1 = derivative(s,f,h)
        ans2 = derivative(s+h,f,h)
        
        if ans1 * ans2 < 0:
            if ans > 0:
                local_max.append(s+h/2)
                
            else:
                local_min.append(s + h/2)
                
        
        s+=h
                
         
    return local_max,local_min



    
    
         
         
        
  
        
        
    
        
        
        