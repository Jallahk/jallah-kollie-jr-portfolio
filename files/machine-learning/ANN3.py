#Extension of Perceptron Class to 3-Layer ANN class
#J. Rauff, March 2025

from math import exp,sqrt

class Perceptron:
    """This perceptron class has sigmoid activation"""
    
    def __init__(self,inputs,bias=0):
        self.inputs=inputs
        self.weights=[]
        self.bias=bias
        
        from random import random
        for i in range(inputs):
            self.weights.append(random()-0.5)
        if self.bias != 0:
             self.weights.append(random()-0.5)  # add a bias input line
      
    
    def outputValue(self,xList,bias):
       total=0
       for i in range(self.inputs):
           total=total+self.weights[i]*xList[i]
       if self.bias !=0:
           total=total+self.bias*self.weights[self.inputs]
       return 1/(1+exp(-total))

    #Grab the weights for word embedding
    def outputValueH(self,xList,bias):
       total=0
       for i in range(self.inputs):
           total=total+self.weights[i]*xList[i]
       if self.bias !=0:
           total=total+self.bias*self.weights[self.inputs]
       return total


class ANN:
    
    def __init__(self,inputs,hidden,outputs,bias=0):
        self.inputs=inputs
        self.hidden=hidden
        self.outputs=outputs
        self.hiddenLayer=[]
        self.outputLayer=[]
        self.bias=bias
        self.outError=[0]*self.outputs
        self.hiddenError=[0]*self.hidden
        self.construct()
    
    def construct(self):
        """Assembles the network"""
        for i in range(self.hidden):
           self.hiddenLayer.append(Perceptron(self.inputs,self.bias))
        
        for i in range(self.outputs):
            self.outputLayer.append(Perceptron(self.hidden,self.bias))
    
    def outputNet(self,item):
        
        #Output of each hidden layer
        self.HLOut=[]
        for node in self.hiddenLayer:
            self.HLOut.append(node.outputValue(item, node.bias))
        
        #Output of each output layer
        self.NetOut=[]
        for node in self.outputLayer:
            self.NetOut.append(node.outputValue(self.HLOut,node.bias))
        
        
    def train(self,trainingExamples,lrate, epochs):
        """Exits after a specified number of epochs.
            Weight updating as described by Noyes"""
        
        for epoch in range(epochs):
                
            for item in trainingExamples:
                self.outputNet(item[:-1])
                actual=self.NetOut
                desired = item[-1]
                #Output error
                for i in range(self.outputs):
                    self.outError[i]= self.NetOut[i]*(1-self.NetOut[i])*(desired[i]-actual[i])
                #Hidden error
                for h in range(self.hidden):
                    total=0
                    for k in range(self.outputs):
                        total = total + self.outError[k]*self.outputLayer[k].weights[h]
                    self.hiddenError[h] = self.HLOut[h]*(1-self.HLOut[h])*total
                #Weight updating
                for k in range(self.outputs):
                    for h in range(self.hidden):
                        self.outputLayer[k].weights[h]= self.outputLayer[k].weights[h] + lrate*self.outError[k]*self.HLOut[h]
                for h in range(self.hidden):
                    for i in range(self.inputs):
                        self.hiddenLayer[h].weights[i]= self.hiddenLayer[h].weights[i] + lrate*self.hiddenError[h]*item[i]  
                    
                    
#Test the net on training data after learning                
def testNet(net,data):
    for item in data:
        net.outputNet(item[:-1])
        print(net.NetOut, item[-1])

def classify(net,item):
    net.outputNet(item)
    print(net.NetOut)
                
                
#Examples   
                
  
XOR=[[1,1,[1]],[1,0,[1]],[0,1,[1]],[0,0,[0]]]

wee=[[0,1.8,[1]],[2,0.6,[1]],[-1.2,1.4,[0]],[0.4,-1,[0]]]           

patterns=[
[1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,[1]],
[0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,[1]],
[1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,[1]],
[1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,[0]],
[0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,[0]],
[1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,[0]]]

               
test=[1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1]

def printPat(pattern):
    i=0
    while i<25:
        print(pattern[i:i+5])
        i=i+5              
adding= [[0,0,[0,0]],[1,0,[0,1]],[0,1,[0,1]],[1,1,[1,0]]]

quadOut=[[0,1,1,1,1,0,1,[1,1,0,1]],[1,1,0,0,0,1,0,[1,0,0,1]], [1,0,0,1,1,1,0,[1,0,1,1]]]                   

quintOut = [[1, 0, 0, 0, 0, 0,[0,.5, 0, 0.5,0,0]],
        [0, 1, 0, 0, 0, 0, [0.5,0,0.5,0,0,0]],
        [0, 0, 1, 0, 0, 0,[0,0.33,0,0.33,0.33,0]],
        [0, 0, 0, 1, 0, 0,[0.5,0,0.5,0,0,0]],
        [0, 0, 0, 0, 1, 0,[0.5,0,0.5,0,0,0]],
        [0, 0, 0, 0, 0, 1,[0,0,0,0,1,0] ]]                
                
                
                
                
                
                
                
                
                
                     