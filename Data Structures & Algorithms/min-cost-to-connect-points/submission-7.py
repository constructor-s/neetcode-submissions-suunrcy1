from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0])
                dist += abs(points[i][1] - points[j][1])
                edges.append(
                    (dist, i, j)
                )
        heapify(edges)
        dsu = list(range(len(points)))
        def find_set_idx(i, dsu):
            if dsu[i] == i:
                return i
            else:
                return find_set_idx(dsu[i], dsu)
        def union_set(a, b, dsu):
            a = find_set_idx(a, dsu)
            b = find_set_idx(b, dsu)
            if a != b:
                dsu[b] = a
        total_dist = 0
        while edges:
            dist, i, j = heappop(edges)

            a = find_set_idx(i, dsu)
            b = find_set_idx(j, dsu)
            if a != b:
                total_dist += dist
                union_set(a, b, dsu)

        return total_dist
