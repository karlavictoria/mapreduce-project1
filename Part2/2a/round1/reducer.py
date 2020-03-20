#!/usr/bin/python
import sys

dict_ABshotresult_count = {}

for line in sys.stdin:
    line = line.strip()
    playerA, playerB, shotresultnum = line.split(',')
    shotresult, num = shotresultnum.split()
    key = playerA+','+playerB+','+shotresult
    try:
        num =int(num)
        dict_ABshotresult_count[key] = dict_ABshotresult_count.get(key,0) + num
    except ValueError:
        pass

for key, value in dict_ABshotresult_count.items():
    print "%s\t%s" % (key, value)
