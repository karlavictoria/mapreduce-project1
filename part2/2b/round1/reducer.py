#!/usr/bin/python
import sys

dict_zoneplayershotresult_count = {}

for line in sys.stdin:
    line = line.strip()
    zone, player, shotresultnum = line.split(',')
    shotresult, num = shotresultnum.split()
    key = zone+','+player+','+shotresult
    try:
        num =int(num)
        dict_zoneplayershotresult_count[key] = dict_zoneplayershotresult_count.get(key,0) + num
    except ValueError:
        pass

for key, value in dict_zoneplayershotresult_count.items():
    print "%s\t%s" % (key, value)