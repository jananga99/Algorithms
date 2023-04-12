# Uses python3

import sys
import queue

MAX = 10 ** 19

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = 1
    for _ in range(len(adj)):
        for u in range(len(adj)):
            if reachable[u]==1:
                for i in range(len(adj[u])):
                    v = adj[u][i]
                    w = cost[u][i]
                    if distance[u] + w < distance[v]:
                        reachable[v] = 1
                        if _ >= len(adj) - 1:
                            shortest[v] = 0
                        distance[v] = distance[u] + w
    for u in range(len(shortest)):
        if shortest[u]==0:
            for v in adj[u]:
                shortest[v] = 0


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
    s = data[0]
    s -= 1
    distance = [10 ** 19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
    f.close()
