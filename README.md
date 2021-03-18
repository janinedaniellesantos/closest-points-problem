Implement the Divide and Conquer and direct approach of the Closest Points problem. Store 100 points in a file. Compare the performance of the two implementations.

**Introduction**
This program implements the Divide and Conquer and Direct Approach (brute force) of the Closest Points problem. Also, there is a file in this project that stores 100 points in a file. 

**Comparing the performance of the two implementations.**
Beginning with my brute force approach, the program shows that I implemented a main for loop that iterates through every single points in the points list (n-1) times and then another nested for loop that iterates through the list and checks for every single point and returns the shortest distance points. Thus making this solution's time complexity = O(n^2) because it is comparing the distances of each pairs before it returns the smallest.

Next with the divide and conquer approach, although I was unable to get my program working, the way I structured the algorithm was in hopes to acheive finding the closest pair of point in O(nlogn). I based my algorithm off of the one learned in class (Divide and Conquer ppt), first we had to divide the points into two subsets so that half the points are on each side. Then , we were to recursively find the pair of points closest in each of the halves. Then we had to merge in O(n) time for the full algorithm to = O(nlogn)


