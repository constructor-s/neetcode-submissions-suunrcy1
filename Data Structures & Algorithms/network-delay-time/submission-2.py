import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        k - source node
        """
        edges = {}
        for u, v, t in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((u, v, t))

        weights = [float("inf")] * n
        h = [(0, k)]

        while h:
            weight, node = heapq.heappop(h)
            # Only visit if there is an improvement, otherwise it is a cycle/less efficient
            if weight < weights[node-1]:
                weights[node-1] = weight
                if node in edges:
                    for u, v, t in edges[node]:
                        heapq.heappush(h, (weight + t, v))
                    
        res = max(weights)
        if res == float("inf"):
            return -1
        return max(weights)
