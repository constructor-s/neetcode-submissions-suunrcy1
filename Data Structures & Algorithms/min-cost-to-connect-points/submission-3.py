from bisect import insort
from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        edges = []
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                # dist = (points[i][0] - points[j][0]) ** 2
                # dist += (points[i][1] - points[j][1]) ** 2
                # dist **= 0.5
                dist = abs(points[i][0] - points[j][0])
                dist += abs(points[i][1] - points[j][1])
                edges.append(
                    (dist, i, j)
                )

        heapify(edges)
        # greedily take the shortest
        visited = []
        total_dist = 0
        while not visited or len(visited[0]) < len(points):
            dist, i, j = heappop(edges)

            # Find which set
            set_idx_i = -1
            set_idx_j = -2
            for idx in range(len(visited)):
                for k in range(len(visited)):
                    if i in visited[k]:
                        set_idx_i = k
                    if j in visited[k]:
                        set_idx_j = k

            if set_idx_i != set_idx_j: # not connected
                total_dist += dist
                if set_idx_i < 0 and set_idx_j < 0:
                    visited.append({i, j})
                elif set_idx_i >= 0 and set_idx_j < 0:
                    visited[set_idx_i].add(j)
                elif set_idx_i < 0 and set_idx_j >= 0:
                    visited[set_idx_j].add(i)
                else: # both >= 0
                    visited[set_idx_i].update(visited[set_idx_j])
                    visited.pop(set_idx_j)

        return total_dist
