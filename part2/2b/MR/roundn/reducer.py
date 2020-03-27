#!/usr/bin/python

import sys

new_centroids = []
dict_centroid_sum_n = {}
content = []

for line in sys.stdin:
     content.append(line)
for line in content:
    line = line.split('\t')
    old_centroid = line[0].replace('[','').replace(']','').split(',')
    values, n = line[1].split(', ')
    shotclock_sum, shotdist_sum, closedefdist_sum = values.split()
    dict_centroid_sum_n.setdefault(str(old_centroid),[]).append([float(shotclock_sum), float(shotdist_sum), float(closedefdist_sum), float(n)])
    

for key in dict_centroid_sum_n:
    shotclock_sum = 0
    shotdist_sum = 0
    closedefdist_sum = 0
    n=0
    for i in range(len(dict_centroid_sum_n[key])):
        shotclock_sum += dict_centroid_sum_n[key][i][0]
        shotdist_sum += dict_centroid_sum_n[key][i][1]
        closedefdist_sum += dict_centroid_sum_n[key][i][2]
        n += dict_centroid_sum_n[key][i][3]
    shotclock_avg = shotclock_sum/n
    shotdist_avg = shotdist_sum/n
    closedefdist_avg = closedefdist_sum/n
    new_centroids.append([shotclock_avg, shotdist_avg,closedefdist_avg])

for i in range(len(new_centroids)):
    for j in range(len(centroid)):
        print(centroid[i][j], end=' ')