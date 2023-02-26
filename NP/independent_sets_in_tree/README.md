# Independent sets in a tree

## Overview
This is a relaxed problem from finding independent sets in a graph. This relaxed problem is in P.  


## Problem statement
Input is given as a tree with edges which has a weight. Problem is to finding an independent set (i.e., a subset of vertices no two of which are adjacent) of maximum size.


## Solution
Dynamic programming can be used to solve this. If D(v) is the maximum weight of a independent set in a subtree rooted at v. Then  
D(v)=max(w(v)+sumGrand, sumChild) where  
W(v) = weight of v  
sumGrand = D(w) sums for all the grandchildren of v  
sumGrand = D(w) sums for all the children of v  


### Implementation
Recursion can be used to sole this easily. But we may have to increase the maximum recursion depth of python in order to solve large problems.