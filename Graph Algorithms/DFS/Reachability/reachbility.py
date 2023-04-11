# Uses python3

def dfs(adj, cur, visited):
    visited[cur] = True
    for v in adj[cur]:
        if not visited[v]:
            dfs(adj, v, visited)


def reach(adj, x, y):
    visited = [False for _ in range(len(adj))]
    dfs(adj, x, visited)
    return 1 if visited[y] else 0


f = open("./tests/2")
input = f.read()
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
x, y = data[2 * m:]
adj = [[] for _ in range(n)]
x, y = x - 1, y - 1
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
print(reach(adj, x, y))
