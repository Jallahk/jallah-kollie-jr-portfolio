from random import gauss,uniform,randint,seed
import numpy as np
seed(43)
nums =[]
for i in range(5000):
    nums.append(gauss(10,2))
    
mean = sum(nums)/len(nums)
stdev = np.std(nums)

dist ={'sd1':0,'sd2':0,'sd3':0}
for x in nums:
    if abs(mean - x) < stdev:
        dist['sd1'] += 1/5000
    if abs(mean - x) < stdev*2:
        dist['sd2'] += 1/5000
    if abs(mean - x) < stdev*3:
        dist['sd3'] += 1/5000

nums = [int(round(x,0)) for x in nums]
counts = {}
for i in range(3,18):
    counts[i]=nums.count(i)