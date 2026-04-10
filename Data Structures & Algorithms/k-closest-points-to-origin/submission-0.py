import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxh = []
        for i in range(len(points)):
            x, y = points[i]
            dist_sq = x * x + y * y
            if len(maxh) < k:
                heapq.heappush_max(maxh, (dist_sq, i))
            else:
                heapq.heappushpop_max(maxh, (dist_sq, i))

        return [points[i] for _, i in maxh]
