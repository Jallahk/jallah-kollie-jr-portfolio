from Guttag14a import *
def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer', 
             'map', 'watch', 'TV', 'coffee_maker', 'diamond_ring', 'emu', 'duck']
    values = [175, 90, 20, 50, 300, 200, 
              300, 125, 200, 110, 600, 65, 110]
    weights = [10, 9, 4, 2, 1, 20, 
               5, 0.25, 20, 8, 0.10, 12, 3]
    items = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items

infile = open('loot.txt', 'r')
name = []
price = []
weight =[]

for line in infile:
    name,price,weight =line.split('/t')
    


# Tests the greedy 
def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print('Total value of items taken is', val)
    for item in taken:
        print('   ', item)

# Runs the greedy algorithm 
def test_greedys(max_weight=30):
    items = build_items()
    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, value)
    print('\nUse greedy by weight to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, weight_inverse)
    print('\nUse greedy by density to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, density)

# Run the tests
test_greedys()