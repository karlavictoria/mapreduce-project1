#!/usr/bin/python

import sys

for line in sys.stdin:
    try:
        line = line.replace('"','').replace(', ',' ').split(",")
        playerA = line[19].title()
        playerB = (line[14].split()[1] + ' ' +  line[14].split()[0])
        shotresult = line[13]
        print "%s\t%s" % (playerA + ',' + playerB + ',' + shotresult,1)
    except IndexError:
        continue
