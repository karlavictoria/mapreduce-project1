#!/usr/bin/python
from operator import itemgetter
import sys

dict_month_count = {}

for line in sys.stdin:
    line = line.strip()
    month, num = line.split('\t')
    try:
        num = int(num)
        dict_month_count[month] = dict_month_count.get(month, 0) + num

    except ValueError:
        pass


sorted_dict_month_count = sorted(dict_month_count.items(), key=itemgetter(1), reverse = True)
for month, count in sorted_dict_month_count:
    print '%s\t%s' % (month, count)
