"""
CS337 Exam 1B Programming Question
I did not consult with anyone or any internet source on the solution to this exam question.
Name: Jallah Kollie                         
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def max(self):
        #checks if the stack is empty
        if self.isEmpty():
            return None 
        #return max value in stack
        return max(self.items)
    
       


    
    
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def max(self):
        #checks if queue is empty
        if self.isEmpty():
            return None
        #return max value in queue
        return max(self.items)

