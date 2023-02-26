
# TSP

## Problem Statement
Here, there is a connected undirected graph, and you need to find the Hamiltonian cycle with the minimum weight. (This can be used for undirecte dgraphs as well with slight changes.)

## Solving TSP

### Algorithms
#### Brute force
If there are n vertices, then there can only (n-1)! paths. Checks all of them, and find the minimum one.
Time complexity = O((n-1)!)  

#### Dynamic programming
For a subset of vertices S ⊆ {1, . . . , n} containing the vertex 1 and a vertex   i ∈ S, let C(S, i) be the length of the shortest path that starts at 1, ends at i and visits all vertices from S exactly once
C({1}, 1) = 0 and C(S, 1) = +∞ when |S| > 1  
for all S ⊆ {1, . . . , n}, C(S, i) = min(C(S, i), C(S-{i}, j)+graph[i][j]) where j is an element of S  
Time complexity = O((n^2)*(2^n))

#### Bound and search
This is DFS but we keep the optimal valu eup to now and does not expand trees which have already the value grater than the optimal.

### Implementations
Here, there are three implementations to solve TSp. 

First, one is the brute force algorithm. Using it is not recommended, as it is very slow.

Second one is the local search (branch and bound). It is faster than brute force but very slower than the next one Therefore using it is also not recommended.

The recommended is using dynamic programming implementation. It runs in much faster than others in the average case.

(Also, there is a tester file which can be used to verify the correctness of an algorithm for TSp by comparing results of that algorithm with the brute force results.)
