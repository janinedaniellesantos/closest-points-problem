Implement the Divide and Conquer and direct approach of the Closest Points problem. Store 100 points in a file. Compare the performance of the two implementations.

**Demo**
https://youtu.be/xOr6LtHqRh8

**Introduction**
This program implements the Divide and Conquer and Direct Approach (brute force) of the Closest Points problem. Also, there is a file in this project that stores 100 points in a file. 

**Comparing the performance of the two implementations.**
Beginning with my brute force approach, the program shows that I implemented a main for loop that iterates through every single points in the points list (n-1) times and then another nested for loop that iterates through the list and checks for every single point and returns the shortest distance points. Thus making this solution's time complexity = O(n^2) because it is comparing the distances of each pairs before it returns the smallest.

Next with the divide and conquer approach, although I was unable to get my program working, the way I structured the algorithm was in hopes to acheive finding the closest pair of point in O(nlogn). I based my algorithm off of the one learned in class (Divide and Conquer ppt), first we had to divide the points into two subsets so that half the points are on each side. Then , we were to recursively find the pair of points closest in each of the halves and returning the sets in sorted order. Then we had to merge in O(n) time for the full algorithm to = O(nlogn)

**Requirements**
If you want to run through the command line make sure that python is installed:

You can chek if you have python by running $ python --version in the command line, this should output something like: Python 3.7.1
If it is not installed
For MacOS it is recommended to install python using Homebrew, to install Homebrew type this into your terminal: $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" more info on homebrew can be found here: https://brew.sh/
Once Homebrew is installed, you can type: brew install python3 on to your terminal to install python
For other OS try this website: https://realpython.com/installing-python/

