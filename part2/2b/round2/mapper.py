#!/usr/bin/python

import sys

dict_zoneplayer_shotresultcount= {}

content =[]

for line in sys.stdin:
    line = line.split(',')
    zone = line[0]
    player = line[1]
    key = zone + ',' + player
    value = line[2].split('\t')
    dict_zoneplayer_shotresultcount.setdefault(key, []).append(value)

for key, value in dict_zoneplayer_shotresultcount.items():
    print "%s\t%s" % (key, value)