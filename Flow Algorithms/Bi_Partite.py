from collections import deque


class MaxMatching:

    def __init__(self):
        self.flow = None
        self.crewsToEnd = None
        self.sourceToFlgihts = None
        self.adj_matrix = None
        self.flightsForCrews = None
        self.numCrews = None
        self.numFlights = None
        self.crewsForFlights = None

    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        self.numFlights = n
        self.numCrews = m

        self.crewsForFlights = [[] for i in range(n)]
        self.flightsForCrews = [[] for i in range(m)]
        self.adj_matrix = adj_matrix

        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j]:
                    self.crewsForFlights[i].append(j)
                    self.flightsForCrews[j].append(i)

        self.sourceToFlgihts = [True for i in range(n)]
        self.crewsToEnd = [True for i in range(m)]

        self.flow = [[0 for _ in range(self.numCrews)] for __ in range(self.numFlights)]

        while True:
            path = self.BFS()
            if len(path) == 0:
                out = [-1 for i in range(self.numFlights)]
                for i in range(self.numFlights):
                    for j in range(self.numCrews):
                        if self.flow[i][j] == 1:
                            out[i] = j
                return out
            self.addFlow(path)

    def addFlow(self, path):
        l = len(path)
        isCrew = True
        self.crewsToEnd[path[l - 1]] = False
        self.sourceToFlgihts[path[0]] = False
        for i in range(l - 1, 0, -1):
            u = path[i - 1]
            v = path[i]
            if isCrew:
                self.adj_matrix[u][v] = -1 * self.adj_matrix[u][v]
                self.flow[u][v] += 1
            else:
                self.adj_matrix[v][u] = -1 * self.adj_matrix[v][u]
                self.flow[v][u] -= 1
            isCrew = not isCrew

    def BFS(self):
        visitedFlights = [False for i in range(self.numFlights)]
        visitedCrews = [False for i in range(self.numCrews)]
        pathToFLights = [[] for i in range(self.numFlights)]
        pathToCrews = [[] for i in range(self.numCrews)]
        q = deque()
        qTypes = deque()
        for i in range(self.numFlights):
            if self.sourceToFlgihts[i]:
                q.append(i)
                qTypes.append("flight")
                visitedFlights[i] = True
                pathToFLights[i] = [i]
        while len(q) > 0:
            cur = q.popleft()
            curType = qTypes.popleft()
            if curType == "flight":
                for cre in self.crewsForFlights[cur]:
                    if not visitedCrews[cre] and self.adj_matrix[cur][cre] == 1:
                        q.append(cre)
                        qTypes.append("crew")
                        pathToCrews[cre] = pathToFLights[cur] + [cre]
                        visitedFlights[cur] = True
            else:
                for fli in self.flightsForCrews[cur]:
                    if not visitedFlights[fli] and self.adj_matrix[fli][cur] == -1:
                        q.append(fli)
                        qTypes.append("flight")
                        pathToFLights[fli] = pathToCrews[cur] + [fli]
                        visitedCrews[cur] = True
                if self.crewsToEnd[cur]:
                    return pathToCrews[cur]
        return []

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
