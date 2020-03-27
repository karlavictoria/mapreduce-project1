import sys
import numpy as np
import random as rd

shotclock =[]
shotdist = []
closedefdist = []
for line in sys.stdin:
    try:
        line = line.replace(', ',' ').split(',')
        shotclock.append(float(line[8]))
        shotdist.append(float(line[11]))
        closedefdist.append(float(line[16]))
    except ValueError:
        continue

X=np.array((shotclock,shotdist,closedefdist), dtype=float).transpose()
m=X.shape[0] 
n=X.shape[1] 
i=rd.randint(0,X.shape[0])
Centroid=np.array([X[i]])
K=4
# calculate initial centroids with Kmeans++
for k in range(1,K):
    D=np.array([]) 
    for x in X:
        D=np.append(D,np.min(np.sum((x-Centroid)**2)))
    prob=D/np.sum(D)
    cummulative_prob=np.cumsum(prob)
    r=rd.random()
    i=0
    for j,p in enumerate(cummulative_prob):
        if r<p:
            i=j
            break
    Centroid=np.append(Centroid,[X[i]],axis=0)

centroid1 = list(Centroid[0])
centroid2 = list(Centroid[1])
centroid3 = list(Centroid[2])
centroid4 = list(Centroid[3])
Centroid = [centroid1,centroid2,centroid3,centroid4]