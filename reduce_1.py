#!/usr/bin/env python
# coding=utf-8

import sys

elem = None
count = 0
summ = 0.0
lines = []
mean = {}

for line in sys.stdin:
    # создаем список из всех строк чтобы потом снова пройтись
    lines.append(line.strip())
    
    features = line.strip().split()
    antiNucleus = int(features[0])
    prodTime = float(features[2])
    
    if elem == antiNucleus:
        count += 1
        summ += prodTime
    else:
        if elem is not None:
            mean[elem] = summ / count
        elem = antiNucleus
        summ = prodTime
        count = 1

# для последнего элемента
mean[elem] = summ / count

# снова проходимся по строкам чтобы вывести рядом среднее значение для этой категории
for line in lines:
    features = line.split('\t')
    antiNucleus = int(features[0])
    eventFile = int(features[1])
    prodTime = float(features[2])
    Pt = float(features[3])
    print ('%s\t%s\t%s\t%s\t%s' % (str(antiNucleus), str(prodTime), str(eventFile), str(Pt), str(mean[antiNucleus])))
    


