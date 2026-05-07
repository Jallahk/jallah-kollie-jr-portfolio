#Review of random

from random import *

#seed(4) #initialize what the random is going to start with
print(randint(5,20))
print(random())#prints a random number between 0 and 1
print(random())

lst = [1,2,3,4,5,6,7,8]
shuffle(lst)#shuffles the list
print(lst)

print(choice(lst))#randomly select something from the list

print(sample(lst,3)) #gives a random sample of the list

print(uniform(12,46)) #generates real numbers

print(gauss(mu=12, sigma=2.3))