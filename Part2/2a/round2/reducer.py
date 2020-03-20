#!/usr/bin/python

import sys
from operator import itemgetter

dict_A_Bhitrate = {}

for line in sys.stdin:
    line = line.replace('[','').replace(']','').replace('"','').replace("'","").split(',')
    playerA = line[0]
    playerB = line[1].split('\t')[0]
    shotresultlist = line[1].split('\t')[1:] + line[2:]
    if len(shotresultlist) == 2 and shotresultlist[0] == 'made':
        hitrate = 1
    elif len(shotresultlist) == 2 and shotresultlist[0] == 'missed':
        hitrate = 0
    elif shotresultlist[0] == 'made':
        hitrate = float(shotresultlist[1])/(float(shotresultlist[1]) + float(shotresultlist[3]))
    else:
        hitrate = float(shotresultlist[3])/(float(shotresultlist[1]) + float(shotresultlist[3]))
    dict_A_Bhitrate.setdefault(playerA, []).append([playerB, hitrate])

for key in dict_A_Bhitrate:
    sorted_dict_A_Bhitrate = sorted(dict_A_Bhitrate[key], key= itemgetter(1))
    for i in range(0,3):
        print "%s\t%s" % (key, sorted_dict_A_Bhitrate[i])
