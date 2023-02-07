class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        self.numCities = n
        self.visitedBFS = None
        self.pathsBFS = None
        self.minEdgeValueInPathForThisVertice = None

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

    def BFS(self):
        self.visitedBFS = [False for i in range(self.numCities)]
        self.pathsBFS = [[] for i in range(self.numCities)]
        self.minEdgeValueInPathForThisVertice = [float('inf') for i in range(self.numCities)]
        OPEN = [0]
        self.visitedBFS[0] = True
        while len(OPEN) > 0:
            cur = OPEN.pop(0)
            for e in self.graph[cur]:
                edge = self.edges[e]
                toVertice = edge.v
                if edge.capacity <= edge.flow:
                    continue
                if not self.visitedBFS[toVertice]:
                    OPEN.append(toVertice)
                    self.visitedBFS[toVertice] = True
                    self.pathsBFS[toVertice] = self.pathsBFS[cur] + [e]
                    self.minEdgeValueInPathForThisVertice[toVertice] = min(self.minEdgeValueInPathForThisVertice[cur],
                                                                           edge.capacity - edge.flow)
                    if toVertice == self.numCities - 1:
                        return self.pathsBFS[toVertice], self.minEdgeValueInPathForThisVertice[toVertice]
        return [], float('inf')


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        if u!=v and u!=vertex_count and capacity!=0:
            graph.add_edge(u - 1, v - 1, capacity)
    return graph

def max_flow(graph, from_, to):
    flow = 0
    shortestPath, flowVal = graph.BFS()
    while len(shortestPath)>0:
        for e in shortestPath:
            graph.add_flow(e, flowVal)
        flow += flowVal
        shortestPath, flowVal = graph.BFS()
    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))