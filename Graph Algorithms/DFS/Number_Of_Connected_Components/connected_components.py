# Uses python3

import sys


def dfs(adj, cur, visited):
    visited[cur] = True
    for v in adj[cur]:
        if not visited[v]:
            dfs(adj, v, visited)


def number_of_components(adj):
    result = 0
    visited = [False for _ in range(len(adj))]
    for i in range(len(adj)):
        if not visited[i]:
            dfs(adj, i, visited)
            result += 1
    return result


f = open("./tests/1")
input = f.read()
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
print(number_of_components(adj))
f.close()
