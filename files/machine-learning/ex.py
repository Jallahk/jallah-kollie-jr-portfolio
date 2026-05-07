# finalP3.py
# Date: 05/09/2025
# Authors: Noah Horner and Kevin Nshuti
# Genetic Algorithm + Perceptron Class Training
# This program compares Genetic Algorithm (GA) and Perceptron Learning Rule
# for training a perceptron to classify 5x5 letter patterns.


from random import uniform, randint, choice
from perceptronFinal import *

""" 
(b) Range of random values:
    We used random.uniform(-1.0, 1.0) to initialize each of the 25 weights. This keeps the weights in a balanced range, giving enough diversity without going
    to extreme values that might cause unstable outputs.
    
(c) Fitness function:
    The fitness of a chromosome is calculated by how many training patterns the perceptron correctly classifies when using the chromosome as its weight vector.
    Since the perceptron uses the identity activation function, its output is a real number. To simulate binary classification, we interpret any output > 0.5 as class 1, and ≤ 0.5 as class 0.
    For each pattern, if this thresholded prediction matches the true label, the chromosome earns one fitness point.
    The final fitness is the total number of correctly classified patterns.


(d) Termination conditions:
    - Max generations: 500
    - Or if we achieve 100% accuracy (i.e., fitness = total number of patterns)

(e) We train the perceptron twice:
    - Once using perceptron.train()
    - Once by setting best weights found by GA

(f) We show testp() results after each training session.

(g) Weight comparison:
    - The Perceptron learning rule converges quickly but may not find global optimum.
    - GA explores the space more but is slower.
"""

NUM_INPUTS = 25
POP_SIZE = 30
GEN_MAX = 500
MUTATION_RATE = 0.1

# GA - Step 1: Generate Population
def generate_population():
    population = []
    for _ in range(POP_SIZE):
        chromosome = []
        for _ in range(NUM_INPUTS):
            weight = uniform(-1.0, 1.0)
            chromosome.append(weight)
        population.append(chromosome)
    return population


# GA - Step 2: Fitness Function
def fitness(chromosome):
    # Threshold: interpret output > 0.5 as class 1, else class 0

    p = Perceptron(NUM_INPUTS, identity)
    p.weights = chromosome
    correct = 0
    for pat in patterns:
        output = p.classify(pat[:-1])
        if (output > 0.5 and pat[-1] == 1) or (output <= 0.5 and pat[-1] == 0):
            correct += 1
    return correct

# GA - Step 3: Selection
def select(pop_with_fit):
    pop_with_fit.sort(key=lambda x: x[1], reverse=True)
    return pop_with_fit[:POP_SIZE]

# GA - Step 4: Crossover
def crossover(p1, p2):
    idx = randint(0, NUM_INPUTS - 1)
    c1 = p1[:idx] + p2[idx:]
    c2 = p2[:idx] + p1[idx:]
    return c1, c2

# GA - Step 5: Mutation
def mutate(chrom):
    new_chrom = chrom[:]
    for i in range(NUM_INPUTS):
        if uniform(0, 1) < MUTATION_RATE:
            new_chrom[i] += uniform(-0.1, 0.1)  
    return new_chrom

# GA Main
population = generate_population()
generation = 0
best_fit = 0
best_chrom = []

while generation < GEN_MAX and best_fit < len(patterns):
    generation += 1
    # Evaluate current population and assign fitness scores
    pop_with_fit = [(chrom, fitness(chrom)) for chrom in population]
    pop_with_fit = select(pop_with_fit)

    best_chrom = pop_with_fit[0][0]
    best_fit = pop_with_fit[0][1]
    if best_fit == len(patterns):
        break

    next_gen = [x[0] for x in pop_with_fit[:10]]  # keep top 10
    while len(next_gen) < POP_SIZE:
        p1, p2 = choice(pop_with_fit)[0], choice(pop_with_fit)[0]
        c1, c2 = crossover(p1, p2)
        next_gen.extend([mutate(c1), mutate(c2)])

    population = next_gen[:POP_SIZE]

print(f"\n=== GA Finished after {generation} generations ===")
print(f"Best GA fitness: {best_fit} / {len(patterns)}\n")

# Test GA-trained Perceptron
p_ga = Perceptron(NUM_INPUTS, identity)
p_ga.weights = best_chrom
print("GA Perceptron test:")
# Print the predicted and expected outputs using the best chromosome
p_ga.testp(patterns)

# Train using learning rule
p_lr = Perceptron(NUM_INPUTS, identity)
epochs = p_lr.train(patterns, alpha=0.7)
print("\nLearning Rule Perceptron test:")
p_lr.testp(patterns)
print(f"\nTrained in {epochs} epochs using Perceptron learning rule.\n")

# Weight Comparison
# Print a sample comparison of first 5 weights between GA and learning rule
print("\nFirst 5 weights (GA vs Learning Rule):")
for i in range(5):
    print(f"Weight {i+1}: GA = {round(p_ga.weights[i], 3)} vs LR = {round(p_lr.weights[i], 3)}")

