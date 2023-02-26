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


class Solution:

    def __init__(self, graph):
        self.graph = graph
        self.numVertices = len(graph)
        self.optimal = INF
        self.optimalPath = []
        self.optimalFound = False

    # cur path contains this vertex
    # Weight cur value includes this vertex
    def dfs(self, vertex, curPath, weightCurValue):
        if len(curPath) == self.numVertices:
            if self.graph[0][vertex] + weightCurValue < self.optimal:
                self.optimal = self.graph[0][vertex] + weightCurValue
                self.optimalPath = [i for i in curPath]
                self.optimalFound = True
        else:
            for u in range(self.numVertices):
                if self.graph[vertex][u] != INF and u not in curPath:
                    newVal = weightCurValue + self.graph[vertex][u]
                    if newVal < self.optimal:
                        self.dfs(u, curPath + [u], newVal)

    def finOptimalPath(self):
        if self.numVertices == 2:
            if self.graph[0][1] != INF:
                return 2*self.graph[0][1], [0,1]
            else:
                return -1, []
        self.dfs(0, [0], 0)
        if not self.optimalFound:
            return -1, []
        return self.optimal, [i+1 for i in self.optimalPath]


filename = './tests/1'
obj = Solution(read_data(filename))
x, y = obj.finOptimalPath()
print_answer(x, y)
