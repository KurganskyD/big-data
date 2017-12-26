#!/usr/bin/env python
# coding=utf-8
import sys  

for line in sys.stdin:
    antiNucleus = line.split(', ')[0]
    eventFile = line.split(', ')[1]
    prodTime = line.split(', ')[10]
    Pt = line.split(', ')[11]
    print('%s\t%s\t%s\t%s' % (antiNucleus, eventFile, prodTime, Pt))
