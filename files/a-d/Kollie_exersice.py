"""Jallah Kollie Program exercise
#1,2,5,13"""

#1) Write a recursive function to compute the factorial of a number 

def fac(n):
    if n !=0: #base case
        return fac(n-1)*n #factorial multiplication
    else:
        return 1

    
print(fac(5))

#2) Write a recursive function to reverse a list

def revlis(lis):
     if len(lis) <=1:#base case
         return lis
     else:
         val = lis.pop() #remove the last thing in the list
         return [val] + revlis(lis) #add it to the front

u = [9,8,6,7]


print(revlis(u))    

#5) Write a recursive function to compute the fibinacci sequence

def fib(n,seq = None):
    if seq == None: 
        seq = [0,1] #base case
    
    if len(seq) < n:
        seq.append(seq[-1]+seq[-2]) #add the last 2 things in the list
        return fib(n,seq)
    return seq

print(fib(8))

#13) Write program that compute pascal triangle
def pascal(row):
    triangle = []
    for i in range(row):
        if i == 0:
            triangle.append([1]) #first row
        else: 
            prev_row = triangle[-1] #the prev list of rows in triangle
            newRow = [1] #start with 1 everytime
            for j in range(len(prev_row)-1): 
                newRow.append(prev_row[j]+ prev_row[j+1]) #get the middle rows
            newRow.append(1) #add 1 to the endf 
            triangle.append(newRow) #add the new row to the triangle
    maxWidth = len('   '.join(map(str,triangle[-1])))
    #make it look nice
    for row in triangle:
        complete = '   '.join(map(str,row)) #convert int to string and join with space between
        print(complete.center(maxWidth)) #center it using the longest row
    

pascal(5)
