"""Creating a bar graph of food preferences from data in food.txt"""


#Import packages
import matplotlib.pyplot as plt
import numpy as np
from random import random


#Read data file and  create foods dictionary and foodList
infile = open('food.txt','r')
foods={}  #Initialize dictionary
foodList =[]  #Initialize foodList
for line in infile:
    if line not in ['EOF']:
        record= line.split()[:-1]
        for food in record:
            if food not in foods:
                foods[food]=1  #Add food as key to dictionary with value 1
                foodList.append(food)  #Add food to foodList
            else:
                foods[food]+=1   #Increment value of key = food
infile.close()

#How many foods are there?
numberOfFoods = len(foods)
    
#Create a list of (food, quantity) pairs using list comprehension           
foodPairs=[(food,foods[food]) for food in foods]

#Sort the pairs by quantity in descending order
foodPairs.sort(key=lambda x:x[1],reverse = False)

#Create plt figure
plt.figure(1)

foodList =[x[0] for x in foodPairs] #A list of food names
quant=[x[1] for x in foodPairs]   #A corresponding list of quantities

q=np.arange(len(foodList))  #Create template for plt bar graph

#Make a list of random colors
colors=[]
for i in range(numberOfFoods):
    colors.append((random(),random(),random()))


#number of bars, height of bars, width of bars,color of bars
plt.bar(q,quant,0.6,color=colors)

#label the bars and the graph
plt.xticks(q,foodList)

plt.xlabel('Food Preference')
plt.ylabel('Votes')
plt.title('What is for lunch?')

#Show the graph
plt.show()