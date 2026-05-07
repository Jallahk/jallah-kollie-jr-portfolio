f = open('voting.txt','r')
lis = []
for i in f:
    lis.append(i)

new = lis.pop(249)
 
newLis = []
newLis.append(new)
yes = newLis.pop(0)
yes1 = str(yes)
yes1.split(',')

print(yes1)



