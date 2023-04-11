# Uses python3

import sys
import queue


def bipartite(adj):
    Q = []
    colors = [0 for i in range(len(adj))]
    for i in range(len(adj)):
        if colors[i]==0:
            colors[i] = 1
            Q.append(i)
            while len(Q):
                x = Q.pop(0)
                for v in adj[x]:
                    if colors[v] == colors[x]:
                        return 0
                    if colors[v] == 0:
                        Q.append(v)
                        colors[v] = -colors[x]
    return 1


if __name__ == '__main__':
    f = open("./tests/2")
    input = f.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
    f.close()
