#Genetic Algorithm
from random import choice,randint

def generatePop(numpop,len_chrom):
    pop = []
    for i in range(numpop):
        c = ''
        for i in range(len_chrom):
            c += choice(['1','0'])
        pop.append(c)
    return pop
        
def fit1(c,goal):
    fit = 0
    for i in range(len(c)):
        if c[i]==goal[i]:
            fit +=1
    return fit   

def assignFitness(pop,f,goal):
    apop =[]
    for c in pop:
        apop.append((c,f(c,goal)))
    apop.sort(key = lambda x: x[1], reverse = True)
    return apop

def mutate(c):
    pt = randint(0,len(c)-1)
    v = choice(['1','0'])
    lc = list(c)
    lc[pt] = v
    return ''.join(lc)

def crossover(c1,c2):
    gene = randint(0,len(c1)-1)
    lc1, lc2 =list(c1),list(c2)
    temp = lc1[gene]
    lc1[gene] = lc2[gene]
    lc2[gene] = temp
    return ''.join(lc1),''.join(lc2)

goal ='000011101110'  #XOR Truth Table

pop = generatePop(15,12)
generations = 0
while goal not in pop and generations < 1000:
    generations +=1
    apop = assignFitness(pop,fit1,goal)
    child1, child2 = crossover(pop[1],pop[2])
    mut = mutate(pop[3])
    pop += [child1,child2,mut]
    apop = assignFitness(pop,fit1,goal)
    apop = apop[:-3]
    
    pop =[x[0] for x in apop]
    
print(pop,generations)

def showChrome(c):
    print('{0}\n{1}\n{2}\n{3}'.format(c[:3],c[3:6],c[6:9],c[9:]))

#showChrome(pop[0])