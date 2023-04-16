# Uses python3
import math


class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.rank = 0


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.weight = w


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def findRoot(i, nodes):
    if nodes[i].parent == -1:
        return i
    return findRoot(nodes[i].parent, nodes)


def Union(u, v, nodes):
    r1 = findRoot(u, nodes)
    r2 = findRoot(v, nodes)
    if r1 != r2:
        if nodes[r1].rank > nodes[r2].rank:
            nodes[r2].parent = r1
        elif nodes[r1].rank < nodes[r2].rank:
            nodes[r1].parent = r2
        else:
            nodes[r1].parent = r2
            nodes[r2].rank += 1


def clustering(x, y, k):
    nodes = []
    n = len(x)
    for i in range(n):
        nodes.append(Node(x[i], y[i], -1))
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append(Edge(i, j, dist(x[i], y[i], x[j], y[j])))
    edges = sorted(edges, key=lambda edge: edge.weight)
    union_num = 0
    for edge in edges:
        if findRoot(edge.u, nodes) != findRoot(edge.v, nodes):
            union_num += 1
            Union(edge.u, edge.v, nodes)
        if union_num > n - k:
            return edge.weight
    return -1.


if __name__ == '__main__':
    f = open('./tests/2')
    input = f.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
    f.close()
