#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.split(",")
    issuedate = line[4].split("/")
    try:
        issuemonth = int(issuedate[0])
        print "%s\t%s"  % (issuemonth,1)
    except ValueError:
        continue
