import sys
import threading

# # This code is used to avoid stack overflow issues
sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    f = open("./tests/1")
    size = int(f.readline())
    tree = [Vertex(w) for w in map(int, f.readline().split())]
    for i in range(1, size):
        a, b = list(map(int, f.readline().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, D):
    if D[vertex] != -1:
        return D[vertex]
    if len(tree[vertex].children) == 0:
        D[vertex] = tree[vertex].weight
        return tree[vertex].weight
    m1 = tree[vertex].weight
    for u in tree[vertex].children:
        if u != parent:
            for w in tree[u].children:
                if w != vertex and w != parent:
                    m1 += dfs(tree, w, u, D)
    m0 = 0
    for u in tree[vertex].children:
        if u != parent:
            m0 += dfs(tree, u, vertex, D)
    D[vertex] = max(m1, m0)
    return max(m1, m0)


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    D = [-1 for i in range(size)]
    return dfs(tree, 0, -1, D)


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
