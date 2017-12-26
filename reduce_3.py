#!/usr/bin/env python
# coding=utf-8

import sys
elem = None
eventFile_count = None
antiNucleus = None
summ = 0.0
count = 0

for line in sys.stdin:
    features = line.strip().split()
    antiNucleus = int(features[0])
    eventFile = int(features[1])
    Pt = float(features[2])
    if elem == antiNucleus:
        eventFile_count.add(eventFile)
        count += 1
        summ += Pt
    else:
        if elem is not None:
            mean = summ / count
            print ('%s\t%s\t%s' % (str(elem), len(eventFile_count), str(mean)))
        eventFile_count = set()
        eventFile_count.add(eventFile)
        elem = antiNucleus
        summ = Pt
        count = 1

mean = summ / count
print ('%s\t%s\t%s' % (str(elem), len(eventFile_count), str(mean)))  