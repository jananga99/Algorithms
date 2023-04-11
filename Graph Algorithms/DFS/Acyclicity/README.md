Outputs 1 if the graph contains a cycle.

Carry on the regular DFS but keep track of parents of the current node.
If the next node is a parent of the current node it is a cycle.