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
        dsu_size = [1] * len(points)
        def find_set_idx(i, dsu):
            if dsu[i] == i:
                return i
            else:
                dsu[i] = find_set_idx(dsu[i], dsu)  # path compression
                return dsu[i]
        def union_set(a, b, dsu, dsu_size):
            a = find_set_idx(a, dsu)
            b = find_set_idx(b, dsu)
            if a == b:
                return False
            else:
                if dsu_size[a] > dsu_size[b]:
                    a, b = b, a # a is gauranteed smaller than b
                dsu[a] = b # the parent of a is b i.e. merge a into b
                dsu_size[b] += dsu_size[a]
                return True
        total_dist = 0
        while edges:
            dist, i, j = heappop(edges)
            if union_set(i, j, dsu, dsu_size):
                total_dist += dist

        return total_dist
