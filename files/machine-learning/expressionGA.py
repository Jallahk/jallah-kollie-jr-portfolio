#Genetic Algorithm to Construct a Function
from random import choice,randint

def generatePop(numpop,len_chrom):
    pop = []
    for i in range(numpop):
        c = ''
        for i in range(len_chrom):
            c += choice(['+','-','*'])
        pop.append(c)
    return pop
        
def value(c,x,y,z,w):
    return eval('('+str(x)+c[0]+ str(y) +')'+c[1]+'('+str(z) +c[2]+str(w) + ')')

def fcn(x,y,z,w):
    return (x+y) - (z*w)

def fitX(c):
    val1 = value(c,2,3,4,5)
    val2 = value(c,4,2,3,1)
    fit = abs(fcn(2,3,4,5)-val1)+abs(fcn(4,2,3,1)-val2)
    return fit   

def assignFitness(pop,f):
    apop =[]
    for c in pop:
        apop.append((c,f(c)))
    apop.sort(key = lambda x: x[1])
    return apop

def mutate(c):
    pt = randint(0,len(c)-1)
    v = choice(['+','-','*'])
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

pop = generatePop(20,3)
generations = 0
while generations < 5:
    generations +=1
    apop = assignFitness(pop,fitX)
    child1, child2 = crossover(pop[1],pop[2])
    mut = mutate(pop[3])
    pop += [child1,child2,mut]
    apop = assignFitness(pop,fitX)
    apop = apop[:-3]
    
    pop =[x[0] for x in apop]
    
print(apop,generations)