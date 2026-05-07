#Bayes Classifier

def probValue(value,fd): #Calculates the probability of a particular class value
    total = 0
    for k in fd:
        if fd[k][-1] == value:
            total += 1
    return total/len(fd.keys())

def attValueList(fd):  #Creates a list of the values taken by each attribute
    numberOfatts = len(fd[0])
    attList=[]
    for i in range(numberOfatts):
        atts =[]
        
        for k in fd:
             if fd[k][i] not in atts:
                atts.append(fd[k][i])
        attList.append(atts)
    return attList
    
def ProbaGivenv(a,i,v,fd): #Calculates the conditional probability of an attribute given a class value
    totalv, totalav = 0,0
    for k in fd:
        if fd[k][-1]==v:
            totalv += 1
            if fd[k][i] == a:
                totalav += 1
    return  totalav/totalv

def Bayes(new,fd):  #Applies the Naive Bayes Classifier
    
    attList = attValueList(fd)
    #print(attList)
    probVlist = [probValue(x,fd) for x in attList[-1]]
    
    Bdict ={}
    for j in range(len(attList[-1])):
        prod = 1
        for i in range(len(new)):
            prod = prod * ProbaGivenv(new[i],i,attList[-1][j],fd)
        b = prod*probVlist[j]
        Bdict[attList[-1][j]]=b
    #Normalize
    
    total = 0
    for k in Bdict.keys():
        total += Bdict[k]
    if total !=0:
        for k in Bdict.keys():
            Bdict[k] = Bdict[k]/total
    
    highProb = 0
    pred = ''
    for k in Bdict.keys():
        if Bdict[k] > highProb:
            highProb = Bdict[k]
            pred = k
    return Bdict,pred


