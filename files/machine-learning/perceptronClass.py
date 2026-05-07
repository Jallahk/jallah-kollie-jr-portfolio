#Perceptron Class 
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
                #case updating with perceptron learning rule
                if actual <=0.99 and  desired==1:
                    trained=False
                    for i in range(self.inputs):
                        self.weights[i]= self.weights[i] + alpha*item[i]  
                
                if actual > 0.01 and  desired==0:
                    trained=False
                    for i in range(self.inputs):
                        self.weights[i]= self.weights[i] - alpha*item[i]       
                
               
        return 'trained in {0} epochs'.format(epochs)         

    def testp(self,pat):
        for p in pat:
            print(self.outputValue(p[:-1]),p[-1])

    def classify(self,item):
        print(self.outputValue(item))
        
#Identity activation function
def identity(x):
        return x

#Step activation function
def step(x):
    if x <=0:
        return 0
    else:
        return 1

#Wee example
wee=[[0,1.8,1],[2,0.6,1],[-1.2,1.4,0],[0.4,-1,0]]
    
OR=[[0,0,0],[0,1,1],[1,0,1],[1,1,1]]

XOR =[[0,0,0],[1,0,1],[0,1,1],[1,1,0]]


patterns=[
[1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1],
[1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0],
[0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0],
[1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]]

test=[1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1]

def printPat(pattern):
    pp = [str(x) for x in pattern]
    i=0
    while i<25:
        print(''.join(pp[i:i+5]))
        i=i+5
        
letters=[[1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1],
         [1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0]]


letterTest=[0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1]
        
triples =[[0.0013359832746976386, 0.5604525936994378, 0.5271908004682678, 1],
          [0.6932989839049629, 0.2893355966992506, 0.506465487269665, 0],
          [0.45489250703344686, 0.6000560656486245, 0.9709100762771555, 1],
          [0.6321236780291375, 0.9911239504997799, 0.6580117748969245, 0],
          [0.09805716377638152, 0.2602402945733783, 0.8288609524378996, 1],
          [0.7450142617176639, 0.18643580071114663, 0.976747399390948, 0],
          [0.05891679593721372, 0.1043265055305852, 0.5726296504103968, 1],
          [0.5164230878384449, 0.49123813017606044, 0.8839312675696572, 0],
          [0.0610411446162516, 0.20011772032376585, 0.7472791467525546, 1],
          [0.9432298303791598, 0.21350571487102665, 0.1600177917582033, 0],
          [0.28115076627510965, 0.830351958668143, 0.701653522687204, 1],
          [0.8976667872706559, 0.9751722815150821, 0.5932734736484441, 0],
          [0.18503401719783752, 0.6040532734287886, 0.0581574526215729, 1],
          [0.7236875061874061, 0.7699950184455332, 0.11389984076553272, 0],
          [0.25574635901835746, 0.6122752609837984, 0.23146276966417678, 1],
          [0.7641984768912995, 0.8352026467331841, 0.7827334753230052, 0],
          [0.08476385148938914, 0.23490152534777287, 0.20588628945760368, 1],
          [0.8017077895222864, 0.0690513812937722, 0.6056033128579207, 0],
          [0.007800228114480667, 0.7680364018463306, 0.5698414551879899, 1],
          [0.720171002472608, 0.485490453802488, 0.9483792781276897, 0]] 


playTennis =[[1,1,1,0,0],[1,1,1,1,0],[0,1,1,0,1],[-1,0,1,0,1],[-1,-1,0,0,1],
             [-1,-1,0,1,0],[0,-1,0,1,1],[1,0,1,0,0],[1,-1,0,0,1],[-1,0,0,0,1],
             [1,0,0,1,1],[0,0,1,1,1],[0,1,0,0,1],[-1,0,1,1,0]]

films =[[1,1,1,1],[1,0,0,0],[1,1,0,1],[0,0,0,1],[0,1,1,0],[0,1,-1,0],[-1,1,0,0],
        [-1,0,1,0],[0,1,0,1],[1,1,0,1]]





























