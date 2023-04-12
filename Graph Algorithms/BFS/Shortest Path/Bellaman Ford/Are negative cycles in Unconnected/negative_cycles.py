#Uses python3

import sys
#Uses python3

import sys

# Uses Bellaman Ford (Duanmic Preogramming)
# Graph can be dis connected

MAX=10**8

def negative_cycle(adj, cost):
    dist = [MAX for i in range(len(adj))]
    dist[0] = 0
    for _ in range(len(adj)):
        for u in range(len(adj)):
            for i in range(len(adj[u])):
                v = adj[u][i]
                w = cost[u][i]
                if dist[u] + w < dist[v]:
                    if _==len(adj)-1:
                        return 1
                    dist[v] = dist[u] + w
    return 0


if __name__ == '__main__':
    f = open("./tests/1")
    input = f.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
    f.close()
