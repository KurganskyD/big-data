#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    line = line.strip()
    features = line.split()
    if float(features[1]) > float(features[4]):
         print(line)