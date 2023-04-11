# Uses python3

import sys
import queue


def distance(adj, s, t):
    Q = []
    shortestLength = [-1 for i in range(len(adj))]
    shortestLength[s] = 0
    Q.append(s)
    while len(Q):
        x = Q.pop(0)
        for v in adj[x]:
            if shortestLength[v]==-1:
                Q.append(v)
                shortestLength[v] = shortestLength[x] + 1
                if v==t:
                    return shortestLength[v]
    return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
    f.close()
