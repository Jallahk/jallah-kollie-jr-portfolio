'''Jallah Kollie 10-12-25'''
import random
import time


Orglis= [random.randint(0,1000) for _ in range(500)]
#make copies of the list
lis1 = Orglis[:]
lis2 = Orglis[:]
lis3 = Orglis[:]

#bubble execution
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
#execution time
bstart = time.time()
bubbleSort(lis1)
bend = time.time()
btot = bend-bstart #check how long it took
print('bubble sort: ', round(btot,3))


#merge sort execcution
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)
            
mstart = time.time()
mergeSort(lis2)
mend = time.time()# check how long it took
mtot = mend-mstart
print('Merge Sort: ',round(mtot,3))

#insertion execution
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
     
Istart = time.time()
insertionSort(lis3)
Iend = time.time()
Itot = Iend-Istart #checking how long it took
print('Insertion Sort: ',round(Itot,3))

#figure out which excecution is faster
if btot < mtot and btot < Itot:
    print('bubble sort is the faster')
elif mtot<btot and mtot<Itot:
    print('merge sort is faster')
else:
    print('Insertion sort is the faster')



