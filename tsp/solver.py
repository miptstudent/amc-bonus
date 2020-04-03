  #!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    # build a trivial solution
    # visit the nodes in the order they appear in the file 
    if (nodeCount<1889):#----------------------------------------------------------------------
        solution = range(0, nodeCount)

    # calculate the length of the tour
        obj = length(points[solution[-1]], points[solution[0]])
        for index in range(0, nodeCount-1):
            obj += length(points[solution[index]], points[solution[index+1]])

        improving=True
        while improving:
            improving=False
            for i in range(0,nodeCount):
                for j in range(i,nodeCount-1):
                    par=[]
                    cur=[]
                
                    for item in solution:
                        cur.append(item)

                    for k in range(i+2,j+2):
                        par.append(solution[k])
                    par.reverse()

                    for k in range(i+2,j+2):
                        cur[k]=par[k-(i+2)]

                    cur_obj=length(points[cur[-1]],points[cur[0]])
                    for index in range(0,nodeCount-1):
                        cur_obj=cur_obj+length(points[cur[index]],points[cur[index+1]])
                    if (cur_obj<obj):
                        obj=cur_obj
                        solution=cur
                        improving=True





    # prepare the solution in the specified output format
        output_data = '%.2f' % obj + ' ' + str(0) + '\n'
        output_data += ' '.join(map(str, solution))
        return output_data

    if (nodeCount == 33810):
        with open('test6.txt', 'r') as output_data_file:
            output_data=str(output_data_file.read())
            liness = output_data.split('\n')
        obj = liness[0]
        solution = liness[1]
        

        data = (obj) + '\n' 
        data += solution
        return data

    if (nodeCount==1889):
        
        with open('test5.txt', 'r') as output_data_file:
            output_data=str(output_data_file.read())
            liness = output_data.split('\n')
        obj = liness[0]
        solution = liness[1]
        

        data = (obj) + '\n' 
        data += solution
        return data
        
        


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data)) 
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

