class MC():
    def __init__(self, label, party):
        self.party = party
        self.label = label
        self.record = []
        
    def vote(self,n):
        return self.record[n-1]
        
    
    def __str__(self):
        return 'Menmber of congress # {0} is a {1}.'.format(self.label, self.party)
    
    
#this is how you do it usng a dictionary
    
'''infile = open('voting.txt', 'r')
CongDict = {}
label = 0
for line in infile:
    label +=1
    linelist = line[:-1].split(',')
    party = linelist[-1]
    record = linelist[:-1]
    CongDict[label]= MC(label,party)
    CongDict[label].record = record
    

infile.close() '''

infile = open('voting.txt', 'r')
Congress = []
label = 0
for line in infile:
    label +=1
    linelist = line[:-1].split(',')
    party = linelist[-1]
    record = linelist[:-1]
    con= MC(label,party)
    con.record = record
    Congress.append(con)
    

infile.close()
    