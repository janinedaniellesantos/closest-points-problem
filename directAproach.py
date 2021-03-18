import sys
import math
import copy

#points = []
#pointsList = open(sys.argv[1], "r")

#for z in pointsList :
    #z = z.strip()
    #x,y = z.split(' ')
    #points.append(x,y)

#finding the distance between two points 
def elucidian(a,b) :
    return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1]-b[1]), 2)) 

#brute force way to find the closest points
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
    return c, d

points = [(1,1), (1,2), (10,20), (1,100), (5,100), (6,6), (7,8), (20,13), (21,44), (112,11)] 
points.sort()
print(points)
c = points[0]
d = points[1]
distance = elucidian(points[0], points[1])

bruteForceAnswer = bruteForce(points)
print("Brute Force Method: The closest pair of points from the list are", bruteForceAnswer)





