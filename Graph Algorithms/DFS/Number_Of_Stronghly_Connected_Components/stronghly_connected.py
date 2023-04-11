# Uses python3


import sys

sys.setrecursionlimit(200000)


def reverseGraph(adj):
    rg = [[] for i in range(len(adj))]
    for u in range(len(adj)):
        for v in adj[u]:
            rg[v].append(u)
    return rg


def dfs(adj, visited, reversePostOrder, x):
    visited[x] = True
    for v in adj[x]:
        if not visited[v]:
            dfs(adj, visited, reversePostOrder, v)
    reversePostOrder.insert(0, x)


def runDfs(adj):
    reversePostOrder = []
    visited = [False for i in range(len(adj))]
    for u in range(len(adj)):
        if not visited[u]:
            dfs(adj, visited, reversePostOrder, u)
    return reversePostOrder


def number_of_strongly_connected_components(adj):
    reverse_graph = reverseGraph(adj)
    reversePostOrder = runDfs(reverse_graph)
    visited = [False for i in range(len(adj))]
    result = 0
    print(reversePostOrder)
    for v in reversePostOrder:
        if not visited[v]:
            dfs(adj, visited, [], v)
            result += 1
    return result


f = open("./tests/2")
input = f.read()
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
print(number_of_strongly_connected_components(adj))
f.close()
