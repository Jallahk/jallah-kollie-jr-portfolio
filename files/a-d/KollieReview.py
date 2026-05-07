'''Jallah Kollie 09-01-2025'''

from collections import Counter
mytext = "learning computer science is not unlike learning any other type of difficult subject matter."

#Write code to do each of the following.
#1. Create a list of the words in mytext in alphabetical order.
#2. Create a string which is the same as mytext except that all the a's are replaced by X's.
#3. Create a dictionary whose keys are letters and whose values are the frequency of that letter in mytext.
#4. Create a string that has the words in mytext in reverse order.
#5. Create a list whose elements are pairs of the form (word, num) where word is a word in mytext and num
#   is the number of letters in word.
#6. Create a string which is the same as mytext except that all the words are written backwards.
#7. Create a 14 X 14 array in which the (i,j)th entry is 1 if the ith and jth words in mytext have the same
#   number of letters and 0 otherwise.


#1
words = mytext.split(' ')
alph_ord = sorted(words)
print(alph_ord)
print()

#2
mutated_str = mytext.replace('a','X')
print(mutated_str)
print()

#3
freq = {}
for letter in mytext:
    if letter not in {' ', '\n'}:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter] += 1
            
letter_freq = list(freq.items())
#sorting by the value which in this case is the freq amount
letter_freq.sort(key = lambda x: x[1], reverse = True)
print(letter_freq)
print()

#4
reverse = " ".join(mytext.split()[::-1])
print(reverse)
print()

#5
lis = mytext.split()
pair = {}

for word in lis:
    pair[word] = len(word)   
pairl = list(pair.items())  
print(pairl)
print()

#6
words = mytext.split()

nl = [w[::-1] for w in words]

revWords = ' '.join(nl)

print(revWords)
print()


#7
matWord = mytext.split()
matrix = []
for i in range(14):
    row = [0]*14
    matrix.append(row)
    for j in range(14):
        if len(matWord[i]) == len(matWord[j]):
            matrix[i][j]+=1
       
print(matrix)
            
        
        
        




    