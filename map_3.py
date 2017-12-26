#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    antiNucleus = line.split()[0]
    eventFile = line.split()[2]
    Pt = line.split()[3]
    print('%s\t%s\t%s' % (antiNucleus, eventFile, Pt))