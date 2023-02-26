import random
from itertools import permutations

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
                return 2 * self.graph[0][1], [0, 1]
            else:
                return -1, []
        self.dfs(0, [0], 0)
        if not self.optimalFound:
            return -1, []
        return self.optimal, [i + 1 for i in self.optimalPath]


def writeRandomTests():
    for i in range(numTests):
        f = open("./random_tests/tests/" + str(i), "w")
        numVertices = random.randint(1, maxNumVertices)
        numEdges = 0
        graph = [[-1 for j in range(numVertices + 1)] for i in range(numVertices + 1)]
        for i in range(1, numVertices + 1):
            for j in range(i + 1, numVertices + 1):
                # if random.randint(0, 1) == 1:
                graph[i][j] = random.randint(minWeight, maxWeight)
                numEdges += 1
        f.write(str(numVertices) + " " + str(numEdges) + "\n")
        for i in range(1, numVertices + 1):
            for j in range(i + 1, numVertices + 1):
                if graph[i][j] != -1:
                    f.write(" ".join(map(str, [i, j, graph[i][j]])))
                    f.write("\n")
        f.close()


def optimal_path(graph):
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


def write_answer(filename, path_weight, path):
    f = open(filename, "w")
    f.write(str(path_weight) + "\n")
    if path_weight == -1:
        return
    f.write(' '.join(map(str, path)) + "\n")
    f.close()


def solveRandomTests():
    for i in range(numTests):
        print("Solving random test ",i)
        obj = Solution(read_data("./random_tests/tests/" + str(i)))
        x, y = obj.finOptimalPath()
        write_answer("./random_tests/tests/" + str(i) + "a", x, y)
        x, y = optimal_path(read_data("./random_tests/tests/" + str(i)))
        write_answer("./random_tests/tests/" + str(i) + "ac", x, y)


def writeReport():
    fr = open("./random_tests/report", "w")
    fr.write("TITLE\n\n")
    for i in range(numTests):
        f1 = open("./random_tests/tests/" + str(i) + "a", "r")
        f2 = open("./random_tests/tests/" + str(i) + "ac", "r")
        x1 = f1.readline().split()[0]
        y1 = f1.readline()
        x2 = f2.readline().split()[0]
        y2 = f2.readline()
        if x1 != x2:
            print("Inequality detected")
            fr.write("Results for test " + str(i) + "\n")
            fr.write("My\n")
            fr.write(x1 + "\n" + y1 + "\n")
            fr.write("Optimal\n")
            fr.write(x2 + "\n" + y2 + "\n")
            fr.write("\n")
        f1.close()
        f2.close()
    fr.close()


numTests = 5
maxNumVertices = 2
minWeight = 1
maxWeight = 100
writeRandomTests()
print("Tests generated")
solveRandomTests()
writeReport()
# filename = './tests/1'
# obj = Solution(read_data(filename))
# x, y = obj.finOptimalPath()
# print_answer(x, y)
