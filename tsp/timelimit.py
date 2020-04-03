#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random
import numpy as np
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])


def length(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


file = open('text.txt', 'r')
fl = file.read()
lines = fl.split('\n')

nodeCount = int(lines[0])

points = []
for i in range(1, nodeCount + 1):
    line = lines[i]
    parts = line.split()
    points.append(Point(float(parts[0]), float(parts[1])))

# build a trivial solution
# visit the nodes in the order they appear in the file
solution = []
arrived = []
matrix = []
# calculate the length of the tour
vertex = 0

matrix.append(1000000000000)

for i in range(1, nodeCount):
    matrix.append(0)
arrived.append(vertex)

for i in range(0, nodeCount-1):
    for j in range(0, nodeCount):
        if(matrix[j]!=1000000000000):
            matrix[j] = length(points[vertex], points[j])
    vertex = matrix.index(min(matrix))
    matrix[vertex]=1000000000000
    arrived.append(vertex)

solution=arrived
obj = length(points[solution[-1]], points[solution[0]])
for index in range(0, nodeCount - 1):
    obj += length(points[solution[index]], points[solution[index + 1]])
# prepare the solution in the specified output format
output_data = '%.2f' % obj + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, solution))
print(output_data)
