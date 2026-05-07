'''jallah Kollie, Program 5-6, 04-21-25'''

from KNN import *
from crossValidation import *
from ClusterCounts import *

ToTacc = 0

#simulates my 10 trials
for i in range(10):   
    separateData(120, 'carB')


    #gives each string a number 
    sdict = {'vhigh':8,'small':1, 'med':6,'high':10, 'low':7, '2':2, '3':3, '4':4,'5more':5, 'more':11, 'big':12}
    
    #reads the file and converts each string to integer 
    infile = open('carBTrain.txt','r')
    FeatD = {}
    iDx = 0
    for line in infile:
        linelist = line[:-1].split(',')
        feat = linelist[:-1]
        strNum = [sdict[x] for x in feat]
        feat2 = strNum + [linelist[-1]]
        
    #creates the feature dictionary
        FeatD[iDx] = feat2
        
        iDx+=1
        
    
    
       
    infile.close()
    
    actualLabels = []
    carTest = []
    infile = open('carBTest.txt','r')
    
    for line in infile:
        linelist = line[:-1].split(',')
        feat = linelist[:-1]
        actualLabels.append(linelist[-1])
        strNum = [sdict[x] for x in feat]
        feat2 = strNum 
        
        carTest.append(feat2)
    infile.close()
        
        
    correct = 0   
    for item in carTest:
        filler,filler2,pred = KNN(item,FeatD,4)
        
        if actualLabels[i] in pred:
            correct+=1
            
        accuracy = correct/len(carTest)
        
        ToTacc += accuracy
        
Macc = ToTacc/10

print('The mean accuracy over 10 trials is: ', round(Macc,4))
print() 
        
        
        
        
  
        
        
#print(BayesEval('f'))          
        
    #print(KNN(carTest,FeatD,4))

   
    




#print(KNN(new,f,4))
    
    
    


    
#part 2
#reads the file and turns data into numbers and add append them to a list
UK = []
infile = open('unknownCar.txt','r')
    
for line in infile:
    Uklist = line[:-1].split(',')
    strNum = [sdict[x] for x in Uklist]
    #feat2 = strNum 
    UK.append(strNum)
infile.close()
#Loops through UK and keeps count of the index and finds the KNN 
for index,i in enumerate(UK):
    result = KNN(i,FeatD,4)
    predicted_class = result[-1]
    
    prediction = ', '.join(predicted_class)
    
    print(f"Unknown car #{index+1} is {prediction}")

print()

'''Im not too confident about my classifcation because i have one of my classification being 2 things
meaning two things got the same amount of votes, not quite sure which one to classify as. Don't know which
class to go with.''' 
    


#part 3
    

#makes the example data for kmeans    
examp = makeExamples(FeatD)

#execute the trykmeans
t = trykmeans(examp,4,200)


#loops through the results of trykmeans and label each clustsers, and displays the # of each type of cars

for index, cluster in enumerate(t):
    print(f"Cluster #{index + 1} contains:")
    
    label_counts = {}
    for ex in cluster.examples:
        label = ex.getLabel()
        label_counts[label] = label_counts.get(label, 0) + 1
    
    for label, count in label_counts.items():
        print(f"{count} items of {label}")
    
    print()  # For spacing between clusters


'''The results reveals the distinct patterns in the distributions between the clusters. In clusters 1 we can
see that the very good rating is more favored than the others with 10 items being very good. The other ratings same to be ballanced except for
the good rating, being the lowest rating at 2. THe very good rating was also the most favored in cluster 2 and 3 with
10 items in cluster 2 and 3. But the least favored rating alternate between the two clusters with cluster two least
favorite being unacceptable and cluster 3 least favorite being acceptable. Cluster 4 on the other hand has a
significant difference from the other clusters, with acceptable and good ratings being the most favored with 12 items
for both and the lowest rating being the very good rating which is the total opposite of the other three clusters.'''



