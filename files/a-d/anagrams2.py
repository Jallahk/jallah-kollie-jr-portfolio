"""Time complexity of functions that test for anagrams"""

#Checking Off
def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


#Sort and compare
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort() #only takes O(n^2) or O(nlogn)
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

#Count and compare
def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


"""Time comparisons"""
from random import choice, shuffle
from time import time
def makeBigStrings(n):
    """produces two anagrams of n letters"""
    alist =list('abcdefghijklmnopqrstuvwxyz')
    biglist=[]
    for i in range(n):
        biglist.append(choice(alist))
    bigstring1 = ''.join(biglist)
    shuffle(biglist)
    bigstring2=''.join(biglist)
    return bigstring1, bigstring2

s1, s2 = makeBigStrings(1000)
start=time()
anagramSolution1(s1,s2)
end=time()
print(end-start)

start=time()
anagramSolution2(s1,s2)
end=time()
print(end-start)

start=time()
anagramSolution4(s1,s2)
end=time()
print(end-start)