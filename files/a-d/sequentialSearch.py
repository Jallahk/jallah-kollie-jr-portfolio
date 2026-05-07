def sequentialSearch(alist, item):
    for pos,num in enumerate(alist):
        if num == item:
            return True,pos
    return print(False)
        


print(sequentialSearch([1,2,3,6,8], 9))