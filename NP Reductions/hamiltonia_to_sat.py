# python3
import itertools


class Solution:
    def __init__(self, numVertices, numEdges, edges):
        self.numVertices = numVertices
        self.numEdges = numEdges
        self.edges = edges
        self.graph = [[False for _ in range(self.numVertices)] for i in range(self.numVertices)]
        for e in edges:
            self.graph[e[0] - 1][e[1] - 1] = True
            self.graph[e[1] - 1][e[0] - 1] = True
        self.clauses = []

    def solve(self):

        self.eachVertexBelongToPath()
        self.eachPathPositionOccupied()
        self.nuDuplicatesInPath()
        self.nuDuplicateLocationsInVertice()
        self.twoSuccessiveVerticesInEdge()

        return self.clauses

    def nuDuplicateLocationsInVertice(self):
        comb = list(itertools.combinations([i for i in range(self.numVertices)], 2))
        for vertice in range(self.numVertices):
            for c in comb:
                self.clauses.append([-self.get1D(vertice, c[0]), -self.get1D(vertice, c[1])])

    def nuDuplicatesInPath(self):
        comb = list(itertools.combinations([i for i in range(self.numVertices)], 2))
        for location in range(self.numVertices):
            for c in comb:
                self.clauses.append([-self.get1D(c[0], location), -self.get1D(c[1], location)])

    def get1D(self, i, j):
        return i * self.numVertices + j + 1

    def eachVertexBelongToPath(self):
        for i in range(self.numVertices):
            self.clauses.append([self.get1D(i,j) for j in range(self.numVertices)])

    def eachPathPositionOccupied(self):
        for i in range(self.numVertices):
            self.clauses.append([self.get1D(j,i) for j in range(self.numVertices)])

    def twoSuccessiveVerticesInEdge(self):
        for i in range(self.numVertices):
            for j in range(i+1,self.numVertices):
                if not self.graph[i][j]:
                    for k in range(self.numVertices-1):
                        self.clauses.append([-self.get1D(i, k), -self.get1D(j, k+1)])
                        self.clauses.append([-self.get1D(j, k), -self.get1D(i, k + 1)])


f = open("./tests/hsat")
n, m = map(int, f.readline().split())
# n = vertices   m = edges
edges = [list(map(int, f.readline().split())) for i in range(m)]
obj = Solution(n, m, edges)
clauses = obj.solve()
print(len(clauses), n*n)
for i in clauses:
    print(" ".join(map(str, i+[0])))