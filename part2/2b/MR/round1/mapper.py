#!/usr/bin/python

import sys

Centroid = [[17.0, 16.0, 4.3], [11.2, 4.0, 6.0], [2.5, 12.0, 4.3], [18.0, 0.4, 2.1]]

dict_cluster_points = {}
for line in sys.stdin:
    try:
        line = line.replace(', ',' ').split(',')
        shotclock = (float(line[8]))
        shotdist = (float(line[11]))
        closedefdist = (float(line[16]))
        minDist = 10000
        for i in range(len(Centroid)):
            distance = (Centroid[i][0]-(shotclock))**2 + (Centroid[i][1]-(shotdist))**2 + (Centroid[i][2]-(closedefdist))**2
            if distance < minDist:
                minDist = distance
                index = i
        cluster = str(Centroid[index])
        dict_cluster_points.setdefault(cluster,[]).append([shotclock,shotdist,closedefdist])
    except ValueError:
        continue

#combiner
for cluster in dict_cluster_points:
    shotclock_sum = 0
    shotdist_sum = 0
    closedefdist_sum = 0
    for i in range(len(dict_cluster_points[cluster])):
        shotclock_sum += dict_cluster_points[cluster][i][0]
        shotdist_sum += dict_cluster_points[cluster][i][1]
        closedefdist_sum += dict_cluster_points[cluster][i][2]
    print "%s\t%s" % (cluster,str(shotclock_sum) +' '+ str(shotdist_sum) + ' ' +str(closedefdist_sum)) +', '+str(len(dict_cluster_points[cluster])-1)
