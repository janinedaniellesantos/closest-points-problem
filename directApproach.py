import sys
import math

points = [(37, 32),(93, 76),(93, 81),(18, 76),(66, 31),(79, 74),(6, 32),(79, 57)] # this is just for testing without text file #= open(sys.argv[1], "r")

#algorithm to find the length between point a and b 
closestPoints = {}
closestPoints["pointOne"] = a[0]
closestPoints["pointTwo"] = b[1]
closestPoints["length"] = math.sqrt(math.pow((pointOne[0]- pointTwo[0]), 2) +
                          math.pow((pointOne[1]-pointTwo[1]), 2)) 

for x in range(len(points)-1):
       for y in range(x+1, len(points)):
            length = math.sqrt(math.pow((points[x][0] - points[y][0]), 2) +
                               math.pow((points[x][1] - points[y][1]), 2)
             if length < closestPoints["length"]:
                closestPoints["pointOne"] = points[x]
                closestPoints["pointTwo"] = array[y]
                closestPoints["length"] = length
    return closestPoints
                               
   
                               
