class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm #pages per minute
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self): #Printer's internal clock
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):  #Is the printer busy?
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):  #Start a new task
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() \
                             * 60/self.pagerate     #Number of seconds to complete task

import random
class Task:
    def __init__(self,time):
        self.timestamp = time  #Time created and put in queue
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):  #How long was the task in the queue?
        return currenttime - self.timestamp
