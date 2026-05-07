#Knapsack Problem using Dynamic Programming

from Guttag14a import *
import numpy as np

def build_items():
    names = ['guitar', 'stereo','laptop']
    values = [1500,3000,2000]
    weights = [1,4,3]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

ItemList = build_items()

start = min(ItemList, key = lambda x: x.get_weight())
ItemList.remove(start)
ItemList = [start]+ItemList

grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for j in range(4):
    grid[0][j]=(start.get_value(), [start.get_name()])

for i in range(1,3):
    for j in range(4):
        grid[i][j]=(0, [])

for i in range(1,3):
    current_item_value = ItemList[i].get_value()
    current_item_weight = ItemList[i].get_weight()
    current_item_name = ItemList[i].get_name()
    
    for j in range(4):
        
        
        if current_item_weight == j+1 and current_item_value > grid[i-1][j][0]:
            grid[i][j] = (current_item_value,[current_item_name])
        
        elif current_item_weight > j+1:
            grid[i][j] = grid[i-1][j]
        
        else:
            option1 = grid[i-1][j][0]
            option2 = current_item_value + grid[i-1][j-current_item_weight][0]
            if option1 > option2:
                grid[i][j] = grid[i-1][j]
            else:
                grid[i][j] = (option2, grid[i-1][j-current_item_weight][1]+[current_item_name])
            

