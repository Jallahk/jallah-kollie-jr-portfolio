'''
By submitting my files, I affirm that the solution to this exam are my own work 
and that I did not consult with anyone human or artificial in writing the code.

Name: Jallah Kollie 

'''

class LimHeap:
    
    def __init__(self,n):
        self.nItem = n
        self.heapList = [0]
        self.currentSize = 0
        
        
    def insert(self,k):
        #insert all n items 
       if self.currentSize < self.nItem:     
                self.heapList.append(k)
                self.currentSize = self.currentSize + 1
                self.percUp(self.currentSize)
          
       else:
           #get the importance rank for comparison
            greatRank = self.heapList[1][0] 
            greatI = 1 
            
            for i in range(1, self.nItem):
                if self.heapList[i][0] > greatRank: #compare to find least significant
                    greatRank = self.heapList[i][0]
                    greatI = i
            
            if k[0] < greatRank: #check and see if the new rank is less than our least significant 
                
                self.heapList[greatI] = k
                #percUp to stabelize the heap
                self.percUp(self.currentSize)
                
                
                
            
          
                
          
              
          
          
      
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i][1] < self.heapList[i // 2][1]: #camparing the values instead of their importance 
              #parent of i is at position i//2
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2  #work your way up the tree
          
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i][1] > self.heapList[mc][1]: 
                
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2][0] < self.heapList[i*2+1][0]:
                return i * 2
            else:
                return i * 2 + 1
            
            
            
            
            
bh = LimHeap(8)
lst=[(5,'antelope'), (4,'bear'), (1,'cat'), (2,'dog'), (3,'elephant'), (2,'frog'), (5,'goat'), (3,'hare')]
for item in lst:
    bh.insert(item)
print(bh.heapList)
bh.insert((3,'cow'))
print(bh.heapList)
bh.insert((6,'slug'))
bh.insert((4,'Lion'))
bh.insert((2,'ox'))
print(bh.heapList)
