import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for fr, to, price in flights:
            if fr not in adj:
                adj[fr] = [(fr, to, price)]
            else:
                adj[fr].append((fr, to, price))

        h = [(0, src, 0)]
        while h:
            cost, node, stops = heapq.heappop(h)
            if node == dst:
                return cost
            for fr, to, price in adj.get(node, []):
                if stops <= k:
                    heapq.heappush(h, (cost+price, to, stops+1))
            
        return -1
