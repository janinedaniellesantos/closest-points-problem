def divideAndConquer(points, c, d, distance):
    length = len(points)
    
    #dividing the list into 2
    half = length/2

    #seperation line so that half of the points are on either side and vice versa
    middle = (points[half])

    left = points[:middle]
    right = points[middle:]

    c,d,distance = divideAndConquer(left,c,d,distance)
    c,d,distance = divideAndConquer(right,c,d,distance)
    c,d,distance = resultsDC(points,middle,c,d,distance)

    return(c,d,distance)

def resultsDC(points,midPoint,c,d,distance):
    resultsDC = []
    length = len(points)
    #half = int (length/2)
    midPoint = points[half]

    r,l = midPoint + int(distance), midPoint-int(distance)
    #for every point in points, find the shortest distance and append those to 
    for i in range (0, len(points)) : 
        if i[0]>r :
            break
        if l <= x[0] <= r:
            resultsDC.append(i)
    
    resultsDC.sort(key=lambda i:i[1])

    for i in range (0, len(points)):
        min = elucidian(resultsDC[x], resultsDC[y])
        if min < distance: 
            c,d = resultsDC[x], resultsDC[y]
            distance = min
    return (c,d, distance)

#pointOne, pointTwo, dist = divideAndConquer(points, c, d, distance)
#print("DNC: The closest pair of points are", pointOne, pointTwo, dist)
