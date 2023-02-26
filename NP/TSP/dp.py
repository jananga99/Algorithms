from itertools import permutations
from itertools import combinations

INF = 10 ** 9


def read_data(filename):
    f = open(filename, "r")
    n, m = map(int, f.readline().split())
    graph = [[float('inf')] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, f.readline().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph


def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def optimal_path(graph):
    n = len(graph)
    C = [[INF for _ in range(n)] for __ in range(1 << n)]
    backtrack = [[(-1, -1) for _ in range(n)] for __ in range(1 << n)]
    C[1][0] = 0
    for s in range(1, n):
        for S in combinations(range(1, n), s):
            S = (0,) + S
            numS = sum([1 << i for i in S])
            for i in S:
                if i != 0:
                    numOtherS = numS ^ (1 << i)
                    for j in S:
                        if i != j:
                            if C[numOtherS][j] + graph[i][j] < C[numS][i]:
                                C[numS][i] = C[numOtherS][j] + graph[i][j]
                                backtrack[numS][i] = (numOtherS, j)
    minVal = INF
    minValIndex = -1
    for i in range(1, n):
        if minVal > C[(1 << n) - 1][i] + graph[0][i]:
            minVal = C[(1 << n) - 1][i] + graph[0][i]
            minValIndex = i
    if minVal == INF:
        return -1, []
    ind1 = (1 << n) - 1
    ind2 = minValIndex
    path = []
    while ind1 != -1:
        path.insert(0, ind2 + 1)
        ind1, ind2 = backtrack[ind1][ind2]
    return minVal, path


filename = './tests/1'
x, y = optimal_path(read_data(filename))
print_answer(x, y)
