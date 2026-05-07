from perceptronClass import *
from ANN3 import *

#first set
letters = [[0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,[0,0]],
           [0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,[0,1]],
           [0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,[1,0]]]

#creates my neural network 
neuralNet = ANN(49,26,2,.1)

neuralNet.train(letters,.1, 8000) 

testNet(neuralNet,letters)



#camparing images 

Bletters = [[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,[0,0]],
            [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,[0,1]],
            [0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,[1,0]]]


testNet(neuralNet,Bletters)


#I used 49 inputs, 26 hidden nodes,2 outputs, and a learning rate of .1   
# (3) using 1000 epochs and above I saw that I got closure to my inteded values, my learning rate was .1

# (4) The network is very accurate
#(6) It did a good job at identifying the images, the numbers for comapring the C image could be a bit better but it works. 


