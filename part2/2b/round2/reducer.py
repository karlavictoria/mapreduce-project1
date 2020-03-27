#!/usr/bin/python

import sys
from operator import itemgetter

dict_playerzone_shotresult = {}
dict_player_zonehitrate = {}

for line in sys.stdin:
    line = line.replace('[','').replace(']','').replace('"','').replace("'","").split(',')
    zone = line[0]
    player = line[1].split('\t')[0]
    shotresultlist = line[1].split('\t')[1:] + line[2:]
    dict_playerzone_shotresult.setdefault(zone + ','+player, []).append(shotresultlist)

for key, shotresultlist in dict_playerzone_shotresult.items():
    zone, player = key.split(',')
    shotresultlist = (str(shotresultlist).replace('[','').replace(']','').split(','))
    for i in range(len(shotresultlist)):
        shotresultlist[i] = shotresultlist[i].replace('\\n','').replace('\n','').replace("\'","").strip('\\').strip()
    if len(shotresultlist) == 2 and shotresultlist[0] == 'made':
        hitrate = 1
    elif len(shotresultlist) == 2 and shotresultlist[0] == 'missed':
        hitrate = 0
    elif shotresultlist[0] == 'made':
        hitrate = float(shotresultlist[1])/(float(shotresultlist[1]) + float(shotresultlist[3]))
    else:
        hitrate = float(shotresultlist[3])/(float(shotresultlist[1]) + float(shotresultlist[3]))
    dict_player_zonehitrate.setdefault(player, []).append([zone, hitrate])
    
for key in dict_player_zonehitrate:
    sorted_dict_player_zonehitrate = sorted(dict_player_zonehitrate[key], key= itemgetter(1), reverse =True)
    print "%s\t%s" % (key, sorted_dict_player_zonehitrate[0])
