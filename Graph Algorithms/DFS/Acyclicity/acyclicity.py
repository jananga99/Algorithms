#Uses python3

import sys


def dfs(adj, cur, visited, parents):
    visited[cur] = True
    for v in adj[cur]:
        if v in parents or not visited[v] and dfs(adj, v, visited, parents+[cur]) == 1:
            return 1
    return 0


def acyclic(adj):
    visited = [False for _ in range(len(adj))]
    for i in range(len(adj)):
        if not visited[i]:
            val = dfs(adj, i, visited, [])
            if val:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
