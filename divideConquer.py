import math

#calculates the ditance between points 
def elucidian(a,b) :
    return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1]-b[1]), 2)) 

#brute force approach 
def bruteForce(coord,pointOne,pointTwo,eluDist) :
    length = len(coord)
    if length == 2 :
        dist = elucidian(coord[0],coord[1])
        if dist < eluDist :
            pointOne,pointTwo = coord[0],coord[1]
            eluDist = dist
    else: 
        for i in (0, length-1) :
            for j in range(i + 1, length) : 
                distance = elucidian(points[i], points[j]) 
                if distance < eluDist : 
                    distance = eluDist
                    pointOne = points[i]
                    pointTwo = points[j]
    return pointOne, pointTwo, eluDist

#array length <= 3 use brute force approach
def divideConquer(coord,pointOne,pointTwo,eluDist) :
    length = len(coord) 
    if length <= (3) : 
        return (bruteForce(coord,pointOne,pointTwo,eluDist)) 

    #dividing the list into 2
    half = length//2

    #seperation line so that half of the points are on either side and vice versa
    middle = coord[half][0]
    leftX = coord[:half]
    rightX = coord[half:]

    pointOne,pointTwo,eluDist = divideConquer(leftX,pointOne,pointTwo,eluDist)
    pointOne,pointTwo,eluDist = divideConquer(rightX,pointOne,pointTwo,eluDist)
    pointOne,pointTwo,eluDist = resultsDC(coord,middle,pointOne,pointTwo,eluDist)
	
    return (pointOne,pointTwo,eluDist)

def resultsDC(coord,midPoint,pointOne,pointTwo,eluDist):
    resultsDC = [] 
    length = len(resultsDC)
    r,l = midPoint + int(eluDist), midPoint - int(eluDist)

    #for every point in points, find the shortest distance and append those to array
    for x in coord:
        if x[0] > r: 
            break
        elif l <=x [0] <= r: resultsDC.append(x)

    resultsDC.sort(key = lambda x:x[1]) 

    for x in range (0,length):
        for y in range (x+1, min ((x+7),length)) :
            dist = elucidian(resultsDC[x],resultsDC[y])
            if dist < eluDist :
                pointOne,pointTwo = resultsDC[x], resultsDC[y]
                eluDist = dist           
    return (pointOne,pointTwo,eluDist)

points = [(1,1), (1,2), (10,20), (1,100), (5,100), (6,6), (7,8), (20,13), (21,44), (112,11), (11,33), (21, 20), (17, 90) , (33,98)] 
points.sort()
pointOne, pointTwo = points[0],points[1] 
eluDist=elucidian (points[0],points[1]) 
cPOne,cPTwo,distance = bruteForce(points,pointOne,pointTwo,eluDist)
#print
print ("Divide and Conquer Approach: The closest pair of points from the list are", cPOne, cPTwo)
