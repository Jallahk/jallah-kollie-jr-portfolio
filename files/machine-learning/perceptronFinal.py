#Perceptron Class for Final Exam Question

from random import random,randint

class Perceptron:
    """A perceptron is defined by its number of inputs and
its activation function"""
    
    def __init__(self,inputs,activationFunction):
        self.inputs=inputs
        self.weights=[]
        self.actFunc = activationFunction
        
        #Weights are initialized with random numbers in [-0.5, 0.5]
        
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
                
               
        return epochs        

    def testp(self,pat):
        for p in pat:
            print(self.outputValue(p[:-1]),p[-1])

    def classify(self,item):
        return self.outputValue(item)
        
#Identity activation function
def identity(x):
        return x


patterns=[
[1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1],
[1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0],
[0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0],
[1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]]

test=[1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1]

#puts data in adjacent
def printPat(pattern):
    pp = [str(x) for x in pattern]
    i=0
    while i<25:
        print(''.join(pp[i:i+5]))
        i=i+5
        



# Binary step activation function
def step(x):
    return 1 if x > 0 else 0

# Training data
trainingSet = [p[:25] + [1] for p in patterns]

# Fitness: number of correct classifications 
def fitness(weights):
    p = Perceptron(25, step)
    p.weights = weights
    score = 0
    for item in trainingSet:
        if p.outputValue(item[:-1]) == item[-1]:
            score += 1
    return score

# Generate initial population with size number of chromosomes
def generate_population(size):
    pop = []
    # _ is a the throw away variable, don't care about the loop variable
    for _ in range(size):
        chromo = []
        for _ in range(25):
            chromo.append(random() * 2 - 1)  # random float in [-1,1]
        pop.append(chromo)
    return pop

# Select top N by fitness
def select_best(population, scores, count):
    selected = []
    for _ in range(count):
        best_index = 0
        for i in range(1, len(scores)):
            if scores[i] > scores[best_index]:
                best_index = i
        selected.append(population[best_index])
        scores[best_index] = -1  # So it's not picked again
    return selected

# Crossover: single-point crossover
def crossover(p1, p2):
    point = randint(1, 24)
    return p1[:point] + p2[point:]

# Mutation
def mutate(chromo, rate=0.2):
    for i in range(25):
        if random() < rate:
            chromo[i] += random() * 0.2 - 0.1  # small change in [-0.1, 0.1]
    return chromo

# Main evolution loop
def evolve(pop_size=50, generations=50, elite_size=10, mutation_rate=0.2):
    population = generate_population(pop_size)
    best_chromo = None
    best_score = -1

    for g in range(generations):
        scores = [fitness(chromo) for chromo in population]
        elite = select_best(population[:], scores[:], elite_size)

        if max(scores) > best_score:
            best_score = max(scores)
            best_chromo = elite[0]
            print("Generation", g, "Best fitness:", best_score)

        # Generate new population
        new_population = elite[:]
        while len(new_population) < pop_size:
            parent1 = elite[randint(0, elite_size - 1)]
            parent2 = elite[randint(0, elite_size - 1)]
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    return best_chromo

# Run GA
best_weights = evolve()

# Use best weights on test pattern
p = Perceptron(25, step)
p.weights = best_weights


#\n moves what is being printed to the next line
print("\nFinal Classification of Training Patterns:")
p.testp(trainingSet)

print("\nTest Pattern:")
printPat(test)
print("\nClassified as:", p.classify(test))


#using identity
print("\nPerceptron Learning Rule")
p1 = Perceptron(25, identity)
epochs = p1.train(patterns, alpha=.4, showWeights=False)
print("Epochs to train:", epochs)
#print("Final Weights (PLR):", p1.weights)
print("Classification:")
p1.testp(trainingSet)
print()
print("Genetic Algorithm")
best_weights = evolve()
p2 = Perceptron(25, identity)
p2.weights = best_weights
#print("Best Weights (GA):", p2.weights)
print("GA Classification:")
p2.testp(trainingSet)




'''


2) For my random range I used -1 to 1 becuase  I didn't want the number to be too big or too little. And
making it go from -1 to 1 instead of 0 to 1 allows for the chromosome to also be a negative number


3) My fitness frunction was the number of training patterns correctly classified by one chromosome


4) My termination rate really doesn't seem to have much of a effect on my result. But when I changed my mutation
rate to something other than .2, I saw that some instances classified the pattern as 0. In which I was able to alter
the generations value to get a better result.

5) A major difference between the weights of the two methods is the fact that PLR has more negative values in its classification, which
could point to there being more negitive weights in the PLR.

''' 




