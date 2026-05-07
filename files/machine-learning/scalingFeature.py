#Scaling data for Nearest Neighbor classification

import numpy as np

def linear_scale(vals):
    """Assumes vals is a sequence of floats"""
    vals = np.array(vals)
    vmin = vals.min() #Needed for new data
    vmax = vals.max() #Needed for new data
    if vmin != vmax:
        vals = (vals - vmin)/(vmax - vmin)
    else:
        vals = vals - vmin
    return vals,vmin,vmax   #returns the scaled data and the factors needed to scale new data

def z_scale(vals):
    """Assumes vals is a sequence of floats"""
    mean = np.array(vals).mean()
    std = np.array(vals).std()
    result = np.array(vals) - np.array(vals).mean()
    if std != 0:
        return result/std,mean,std
    else:
        return result,mean,std

#Linear scaling: Linearly scales all the data
def linscale(fd):
    """Assumes fd is a feature dictionary"""
    fl={}
    for k in fd.keys():
        fl[k]=fd[k].copy()
    scaleFactors = []
    for col in range(len(fl[0])-1):
        templist = []
        for i in fl.keys():
            templist.append(fl[i][col])
        templist,vmin,vmax = linear_scale(templist)
        scaleFactors.append([vmin,vmax-vmin])
        for i in fl.keys():
            fl[i][col]=templist[i]
    return fl,scaleFactors

#Use this function to scale new data based upon old data       
def linscaleNew(new, scaleFactors):
    lnew = new.copy()
    for i in range(len(new)):
        if scaleFactors[i][1] != 0:
            lnew[i] = (lnew[i]-scaleFactors[i][0])/(scaleFactors[i][1])
        else:
            lnew[i] = lnew[i]-scaleFactors[i][0]
    return lnew


#Z-scaling
def zscale(fd):
    """Assumes fd is a feature dictionary"""
    f={}
    for k in fd.keys():
        f[k]=fd[k].copy()
    scaleFactors = []
    for col in range(len(f[0])-1):
        templist = []
        for i in f.keys():
            templist.append(f[i][col])
        templist,mu,sigma = z_scale(templist)
        scaleFactors.append([mu,sigma])
        for i in f.keys():
            f[i][col]=templist[i]
    return f,scaleFactors

#Z-scales a new item
def zscaleNew(new, scaleFactors):
    znew = new.copy()
    for i in range(len(new)):
        if scaleFactors[i][1] != 0:
            znew[i] = (znew[i]-scaleFactors[i][0])/(scaleFactors[i][1])
        else:
            znew[i] = znew[i]-scaleFactors[i][0]
    return znew

