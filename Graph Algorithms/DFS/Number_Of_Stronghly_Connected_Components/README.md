Finds the number of strongly connected components in the graph.

Algorithm is quite complex

1. Reverses the graph.
2. Get reverse post order of nodes in the reverse graph.
3. Iterate though this post order and apply dfs to unvisited nodes
   Count how many forests are there.
    It is the number of strongly connected components.