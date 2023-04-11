# Uses python3


def dfs(adj, used, order, x):
    used[x] = True
    for v in adj[x]:
        if not used[v]:
            dfs(adj, used, order, v)
    order.insert(0, x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if not used[i]:
            dfs(adj, used, order, i)
    return order


f = open("./tests/2")
input = f.read()
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
order = toposort(adj)
for x in order:
    print(x + 1, end=' ')
f.close()
