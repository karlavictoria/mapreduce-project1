#!/usr/bin/python

import sys

dict_AB_shotresultcount= {}

for line in sys.stdin:
    line = line.split(',')
    playerA = line[0]
    playerB = line[1]
    key = playerA + ',' + playerB
    value = line[2].split()
    dict_AB_shotresultcount.setdefault(key, []).append(value)

for key, value in dict_AB_shotresultcount.items():
    print "%s\t%s" % (key, value)
