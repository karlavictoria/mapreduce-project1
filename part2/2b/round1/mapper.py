#!/usr/bin/python

import sys

Centroid1 = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
Centroid2 = [float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])]
Centroid3 = [float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9])]
Centroid4 = [float(sys.argv[10]), float(sys.argv[11]), float(sys.argv[12])]

Centroid = [Centroid1,Centroid2,Centroid3,Centroid4]

for line in sys.stdin:
    try:
        line = line.replace(', ',' ').split(',')
        shotclock = (float(line[8]))
        shotdist = (float(line[11]))
        closedefdist = (float(line[16]))
        player = line[19].title()
        shotresult = line[13]
        minDist = 10000
        for i in range(len(Centroid)):
            distance = (Centroid[i][0]-(shotclock))**2 + (Centroid[i][1]-(shotdist))**2 + (Centroid[i][2]-(closedefdist))**2
            if distance < minDist:
                minDist = distance
                index = i
        zone = 'Zone'+str(index+1)
        print "%s\t%s" % (zone + ',' + player + ',' + shotresult, 1)
    except ValueError:
        continue