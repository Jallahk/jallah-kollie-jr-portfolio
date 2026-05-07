#Perceptron Class with Delta Rule
#A simple perceptron class with examples
#J. Rauff -- March 2025

class Perceptron:
    """A perceptron is defined by its number of inputs and
its activation function"""
    
    def __init__(self,inputs,activationFunction):
        self.inputs=inputs
        self.weights=[]
        self.actFunc = activationFunction
        
        #Weights are initialized with random numbers in [-0.5, 0.5]
        from random import random
        for i in range(inputs):
            self.weights.append(random()-0.5)
        
        
    
    def outputValue(self,xList):
        """returns the output from the input list"""
        total=0
        for i in range(self.inputs):
            total=total+self.weights[i]*xList[i]
       
        return self.actFunc(total)

    def train(self,trainingSet,alpha = 1,showWeights =False):
        """trains the perceptron on a training set"""
        trained=False
        epochs=0
        
        while not trained:
            if showWeights: print(self.weights) 
            epochs+=1
            trained=True
            for item in trainingSet:
                actual =  self.outputValue(item[:-1])
                desired =item[-1]
                #case updating with Delta learning rule
                if actual != desired:
                    trained=False
                    for i in range(self.inputs):
                        self.weights[i]= self.weights[i] + alpha*(desired - item[i]*self.weights[i])*item[i]  
                
                   
                
               
        return 'trained in {0} epochs'.format(epochs)         


#Step activation function (bipolar)
def step(x):
    if x <=0:
        return -1
    else:
        return 1

from math import exp
#Discrete sigmoid activation function
def sigmoid(x):
    v = 1/(1+exp(3-6*x))
    if v < 0.5:
        return -1
    else:
        return 1
    
#Wee example
wee=[[0,1.8,1],[2,0.6,1],[-1.2,1.4,-1],[0.4,-1,-1]]
    
OR=[[0,0,-1],[0,1,1],[1,0,1],[1,1,1]]

XOR =[[0,0,0],[1,0,1],[0,1,1],[1,1,0]]


patterns=[
[1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1],
[1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,-1],
[0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,-1],
[1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,-1]]

test=[1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1]



def testp(p,pat):
    '''Tests a trained perceptron p on pattern set pat'''
    for pp in pat:
        print(p.outputValue(pp[:-1]),pp[-1])

def printPat(pattern):
    pp = [str(x) for x in pattern]
    i=0
    while i<25:
        print(''.join(pp[i:i+5]))
        i=i+5
        
letters=[[1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1],
         [1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,-1]]


letterTest=[0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1]
        

