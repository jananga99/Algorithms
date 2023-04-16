# Uses python3
import heapq
import sys
import math


def minimum_distance(x, y):
    def dist(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    visited = [False for _ in range(len(x))]
    visitedCount = 1
    result = 0
    visited[0] = True
    heap = [(dist(x[0], y[0], x[i], y[i]), i) for i in range(1, len(x))]
    heapq.heapify(heap)
    while visitedCount < len(x):
        d, i = heapq.heappop(heap)
        if not visited[i]:
            visited[i] = True
            visitedCount += 1
            result += d
            for j in range(len(x)):
                if j != i and visited[j] == False:
                    heapq.heappush(heap, (dist(x[i], y[i], x[j], y[j]), j))
    return result


if __name__ == '__main__':
    f = open('./tests/1')
    input = f.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    f.close()
