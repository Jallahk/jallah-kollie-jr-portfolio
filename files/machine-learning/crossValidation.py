#Holdout Cross-Validation 

#Making training and test files
from random import randint
from naiveBayes import *

def separateData(testSize,file_prefix):
    original = file_prefix + '.txt'
    train = file_prefix + 'Train.txt'
    test = file_prefix + 'Test.txt'
    infile = open(original,'r')
    outtrain = open(train,'w')
    outtest = open(test,'w')
    counter = 0
    for line in infile:
        flip = randint(1,2)
        if flip == 1:
            if counter < testSize:
                print(line[:-1], file = outtest)
                counter+=1
            else:
                print(line[:-1], file = outtrain)
        else:
            print(line[:-1],file = outtrain)
    infile.close()
    outtrain.close()
    outtest.close()

def BayesEval(file_prefix):
    fd = {}
    ID = 0
    infile=open(file_prefix +'Train.txt','r')
    for line in infile:
            fd[ID] = line[:-1].split(',')
            ID+=1
    infile.close()
    
    testList =[]
    actValueList =[]
    infile = open(file_prefix+'Test.txt','r')
    for line in infile:
        rec = line[:-1].split(',')
        testList.append(rec[:-1])
        actValueList.append(rec[-1])
    infile.close()

    correct = 0
    for i in range(len(testList)):
        _,pred = Bayes(testList[i][:-1],fd)
        if pred == actValueList[i]:
            correct += 1
    accuracy = correct/len(testList)
    return round(accuracy,4)