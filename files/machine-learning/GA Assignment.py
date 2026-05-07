
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

#puts data in adjacency matrix
def printPat(pattern):
    pp = [str(x) for x in pattern]
    i=0
    while i<25:
        print(''.join(pp[i:i+5]))
        i=i+5
        



# Fitness function for coloring
def fitness(coloring):
    conflicts = 0
    used_colors = set()

    for i in range(25):
        used_colors.add(coloring[i])
        row, col = divmod(i, 5)
        neighbors = []

        if row > 0: neighbors.append(i - 5)
        if row < 4: neighbors.append(i + 5)
        if col > 0: neighbors.append(i - 1)
        if col < 4: neighbors.append(i + 1)

        for neighbor in neighbors:
            if coloring[i] == coloring[neighbor]:
                conflicts += 1

    conflicts = conflicts // 2
    return 10 * conflicts + len(used_colors)

# Generate initial population of colorings
def generate_population(size, max_colors=5):
    pop = []
    for _ in range(size):
        chromo = [randint(0, max_colors - 1) for _ in range(25)]
        pop.append(chromo)
    return pop

# Select top N
def select_best(pop, scores, n):
    best = []
    for _ in range(n):
        best_index = 0
        for i in range(1, len(scores)):
            if scores[i] < scores[best_index]:  # minimize
                best_index = i
        best.append(pop[best_index])
        scores[best_index] = float('inf')
    return best

# Crossover
def crossover(p1, p2):
    point = randint(1, 24)
    return p1[:point] + p2[point:]

# Mutation
def mutate(chromo, rate=0.2, max_colors=5):
    for i in range(25):
        if random() < rate:
            chromo[i] = randint(0, max_colors - 1)
    return chromo

# Evolution loop
def evolve_colors(pop_size=50, generations=100, elite_size=10, mutation_rate=0.2, max_colors=5):
    population = generate_population(pop_size, max_colors)
    best = None
    best_score = float('inf')

    for g in range(generations):
        scores = [fitness(chromo) for chromo in population]
        elite = select_best(population[:], scores[:], elite_size)

        current_best_score = min(scores)
        if current_best_score < best_score:
            best_score = current_best_score
            best = elite[0]
            print(f"Generation {g}, Best fitness: {best_score}")

        new_pop = elite[:]
        while len(new_pop) < pop_size:
            p1 = elite[randint(0, elite_size - 1)]
            p2 = elite[randint(0, elite_size - 1)]
            child = crossover(p1, p2)
            child = mutate(child, mutation_rate, max_colors)
            new_pop.append(child)

        population = new_pop

    return best

# Use it on test pattern
best_coloring = evolve_colors()

# Display result
print("\nBest Coloring (by node index):")
print(best_coloring)
print("Fitness Score:", fitness(best_coloring))

# Optional: visual grid
def show_coloring_grid(coloring):
    for i in range(0, 25, 5):
        print(' '.join(str(coloring[j]) for j in range(i, i+5)))

print("\nColoring Grid:")
show_coloring_grid(best_coloring)
        
        
  
