import sys
import math
#is numpy general library?? 

def elucidian(a,b) :
    return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1]-b[1]), 2)) 

def bruteForce(points) : 
    c = points[0]
    d = points[1] 
    minDist = elucidian(c,d)
    for i in (0, len(points)-1):
        for j in range(i + 1, len(points)): 
            distance = elucidian(points[i], points[j]) 
            if distance < minDist: 
                distance = minDist
                c = points[i]
                d = points[j]
    return distance, c, d

points = [(1,1), (1,1), (1,100), (5,100)] # this is just for testing #text file = open(sys.argv[1], "r")
points.sort()
a = bruteForce(points)
print("The closest pair of points are", a)


