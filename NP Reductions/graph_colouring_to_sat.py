# python3


class Solution:
    def __init__(self, n, m, edges):
        self.n = n  # number of vertices
        self.m = m  # number of edges
        self.edges = edges

    def solve(self):
        numVariables = 3 * self.n
        numConstraints = 3 * self.m + self.n
        for i in range(1,self.n+1):
            print(3*i,3*i-1,3*i-2,0)
        print(numConstraints, numVariables)
        for i in range(self.m):
            edge = self.edges[i]
            for k in range(3):
                print(-3*edge[0]+k,-3*edge[1]+k,0)


f = open("./tests/gcts")
n, m = map(int, f.readline().split())
edges = [list(map(int, f.readline().split())) for i in range(m)]
f.close()
obj = Solution(n, m, edges)
obj.solve()
