#Uses python3

import sys
import queue
import heapq


def distance(adj, cost, s, t):
    heap = []
    heapq.heappush(heap, (0, s))
    dist = [float('inf') for i in range(len(adj))]
    dist[s] = 0
    while heap:
        d,u = heapq.heappop(heap)
        for i in range(len(adj[u])):
            v = adj[u][i]
            w = cost[u][i]
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    if dist[t] == float('inf'):
        return -1
    return dist[t]


if __name__ == '__main__':
    f = open("./tests/3")
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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
    f.close()
