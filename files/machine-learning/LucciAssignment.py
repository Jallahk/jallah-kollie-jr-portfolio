from perceptronClass import *
from random import random,shuffle

tripple = []

#add 20 random set of 3 numbers to a list
for i in range(20):
    if i<=10:
        x = random()
        y = random()
        z = random()
        tripple.append([x,y,z,0])
       
       #split the numbers so it is linearly seperable 
    else:
        x = random()
        y = random()
        z = random()-1
        tripple.append([x,y,z,1])
    


#creates the alpha values
alpha = [.01,.1,.25,.50,1.0,5.0]
shuffle(tripple)

#finds the perceptron 
for i in alpha:
   
    P = Perceptron(3,identity)
    print(f'If the alpha is {i} then it is',P.train(tripple,i))






#when using the alpha value of .01, the machine training took longer. usually 10 or more epochs. As the apla gets larger the epochs decreased