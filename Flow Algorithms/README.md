# Flow Algorithms to find maximum/minimum flow

## Ford Fulkerson Algorithm  
Starts with a zero flow. Then repeatedly adding flow until you cannot add more. Suppose, you have flow f. Then complete the residual graph. Find a new flow g for the residual graph i.e. find a path from source to sink. If such path exists then new flow = f+g. if such path does not exist, then this is the maximum flow.

### Time Complexity
f = Maximum Flow  
E = Number of edges
Time complexity = O(|f||E|)

## Edmond Kurp Algorithm
Edmond Kurp is an improvement of Ford-Fulkerson algorithm where always selects the shortest augmenting path(smallest number of edges). Therefore, Edmond Kurp uses BFS instead of DFS.

### Time Complexity
V = Number of vertices  
E = Number of edges
Time complexity = O(|V||E|^2)

## Bi partitie problem  
There is a bi partite graph. We need to select the maximum  number of edges in a way that no two such edges connected to the sam vertice.  
This can be modeled as follws. Suppose left set of vertices in left of graph is A, and right of graph is B. Consider the new graph G1, such that each vertice in A is connected to a source named S1 and each vertice in B is connected to sink named S2. Assume each edge maximum flow size is 1. The problem is finding the maximum flow of the G1. This can be done easily using above algorithms. Then, we can select the edges with a flow as the final solution. 

