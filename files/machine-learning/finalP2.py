'''Jallah Kollie
   Juan DelaPuente
final program 2, May 13, 2025'''

'''fuzzy logic is a way of mimicing how humans solve problems by encoding
expireice based knowledge in the form of logical rules - (my notes)

the compliment of µB tell us about the elements that are not in the fuzzy set. So .75 is the degree of non
membership.

'''

import matplotlib.pyplot as plt

#creats muA function
def muA(x):
    if x <=-4:
        return 1
    
    elif x >= -4 and x <= 0:
        return round(-0.25 * x,2)
    
    else:
        return 0
    
    
    
def muB(x):
    if x >=-2 and x <= 0:
        return round(0.5*x +1,2)
    
    elif x >= 0 and x <= 2:
        return round(-0.5*x +1,2)
    
    else:
        return 0
    
    

def muC(x):
    
    if x >= 0 and x <= 5:
        return round(0.20 * x,2)
    
    elif x >=5:
        return 1
    
    else:
        return 0
    
    
# Drawing the graph of membership function on interal [-6,6]

#creats x coordinates
x_vals = [i for i in range(-6,7)] 
    
Aval = [muA(x) for x in x_vals]
    
Bval = [muB(x) for x in x_vals]

Cval = [muC(x) for x in x_vals]



#this plots the graph using the interval as the x coordinates and the fuzzy values as the y coord.
plt.plot(x_vals,Aval, label = 'µA', color = 'red')
plt.plot(x_vals,Bval, label = 'µB', color = 'blue')
plt.plot(x_vals,Cval, label = 'µC', color = 'green')
#makes graph title
plt.title('Membership Functions')

#label and legend, the legend serves as the identifier and is set to default when picking loc on the graph
plt.xlabel('Interval')
plt.ylabel('membership values')
plt.legend()
plt.show()


#sweetness function returns triple expressing membership in three sets
def sweetness(n):
    var = (muA(n),muB(n),muC(n))
    return var

#sweetness(1)


#creates my fuzzy union
def fuzU(fuzzy,logic):
    union = []
    if isinstance(fuzzy,(list,tuple)) and isinstance(logic,(list,tuple)):
        for i in range(len(fuzzy)):
            if fuzzy[i] >= logic[i]:
                union.append(fuzzy[i])
                
            else:
                union.append(logic[i])
                
    else:
        if fuzzy >= logic:
            union.append(fuzzy)
            
        else:
            union.append(logic)
            
    return union
                
            
#print(fuzU(sweetness(1),sweetness(2)))




#creates the fuzzy intercept, taking the minimun of both sets
def fuzInt(fuz,log):
    intercept = []
    if isinstance(fuz,(list,tuple)) and isinstance(log,(list,tuple)):
        for i in range(len(fuz)):
            if fuz[i] >= log[i]:
                intercept.append(log[i])
                
            else:
                intercept.append(fuz[i])
                
    else:
        if fuz >= log:
            intercept.append(log)
            
        else:
            intercept.append(fuz)
            
    return intercept
                
            
#print(fuzInt(sweetness(-2),sweetness(1)))


#calculate the fuzzy compliment
def fuzComp(memSet):
    comp = []
    if isinstance(memSet,(list,tuple)):
        for i in range(len(memSet)):
            comp.append(1-memSet[i])
    else:
        comp.append(1-memSet)
    return comp

print(fuzComp(muB(1.5)))

'''the compliment of µB tell us about the elements that are not in the fuzzy set. So .75 is the degree of non
membership.'''