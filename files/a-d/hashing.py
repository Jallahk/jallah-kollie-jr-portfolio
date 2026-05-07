"""Hashing"""

class hashTable():
    def __init__(self,size,hashfunction):
        self.table =[None]*size
        self.size =size
        self.hashfunction=hashfunction

    def putInTable(self, item):
        key=self.hashfunction(item,self.size)
        self.table[key]=item
    
    def searchTable(self,item):
        key = self.hashfunction(item,self.size)
        if self.table[key]==item:
            return True
        else:
            return False
        
    def loadFactor(self):
        return round((self.size - self.table.count(None))/self.size,2)
    
    def __str__(self):
        return str(self.table)

#Hash functions take two parameters: an item and the hashtable size

def  simpleHash(item,tablesize):
    return item%tablesize

def strHash(astring, tablesize):
    sumch = 0
    for pos in range(len(astring)):
        sumch = sumch + ord(astring[pos])
    return sumch%tablesize   

#Examples        
bob=hashTable(11,simpleHash)
for num in [63,3,64,17,5]:
    bob.putInTable(num)
print(bob)
print(bob.searchTable(645))
print(bob.searchTable(45))

ray=hashTable(13,strHash)
for name in ['yoda','luke', 'r2d2','chewy']:
    ray.putInTable(name)
print(ray)
print(ray.searchTable('yoda'))
print(ray.searchTable('han'))
