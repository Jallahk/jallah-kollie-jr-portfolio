'''Jallah Kollie Radix program.
   September 10 2025'''

#ones place -> x%10  hundreds place -> (x//100)%10  tens -> (x//10)%10 
from QueueClass import Queue
import random
#first make a list of random numbers
main = [random.randint(0,999) for _ in range(10)]
print('Unsorted: ', main)

#create the bins
bins = [Queue() for _ in range(10)]

order = False
placeVal = 1
while not order:
    #loop through a copy of the list taking each element out and put it in a bin
    for num in main[:]:
        numOut = num
        #identify the place value # of each item that is taken out of the list
        val = (numOut//placeVal)%10
        bins[val].enqueue(numOut)
   
    #empty the main bin        
    main.clear()
   
    for queue in bins:
        #put them back in the main starting from bin 0-9
        while not queue.isEmpty():
            main.append(queue.dequeue())
    #checks if they are sorted right
    if main == sorted(main):
        order = True
               
    else:
        #changes the place value
        placeVal *=10
                        
print('Sorted: ',main)          
            