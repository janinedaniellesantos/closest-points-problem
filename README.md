Implement the Divide and Conquer and direct approach of the Closest Points problem. Store 100 points in a file. Compare the performance of the two implementations.

**Demo**
https://youtu.be/xOr6LtHqRh8

**Introduction**
This program implements the Divide and Conquer and Direct Approach (brute force) of the Closest Points problem. Also, there is a file in this project that stores 100 points in a file. 

**Comparing the performance of the two implementations.**
Beginning with my brute force approach, the program shows that I implemented a main for loop that iterates through every single points in the points list (n-1) times and then another nested for loop that iterates through the list O(n) and checks for every single point and compares two points and returns the shortest distance points. Thus making this solution's T(n) = O(n^2) because it is comparing the distances of each pairs before it returns the smallest.

Next with the divide and conquer approach, the way I structured the algorithm was in hopes to acheive finding the closest pair of point in O(nlogn). I based my algorithm off of the one learned in class (Divide and Conquer ppt). Let's first establish that my program had a points array with all x,y xoordinates. 

We first had to divide the points array into two parts, the first part takes care of points from ppoint[0] to points[n/2] and the second from points[n/2+1] to 
P[n-1]. After the array was divided in 2 parts, the program uses a divideConquer function that recursively calls itself on first the left half then the right half, this function also uses the resultsDC function wich initializes another array that stores the shortest points from the middle but the resultDC array is filled in O(n) time with a for loop in the resultsDC function. The resultsDC array is sorted in O(nLogn) time and then finds the closes pair of points in O(n) times through the divide and conquer function. So T(n) = 2T(n/2)+O(nLogn) = T(nLognLogn)

**Requirements**
If you want to run through the command line make sure that python is installed:

You can chek if you have python by running $ python --version in the command line, this should output something like: Python 3.7.1
If it is not installed
For MacOS it is recommended to install python using Homebrew, to install Homebrew type this into your terminal: $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" more info on homebrew can be found here: https://brew.sh/
Once Homebrew is installed, you can type: brew install python3 on to your terminal to install python
For other OS try this website: https://realpython.com/installing-python/

