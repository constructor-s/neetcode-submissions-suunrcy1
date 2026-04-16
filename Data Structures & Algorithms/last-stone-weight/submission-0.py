import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones) # O(n)
        while len(stones) > 1:
            y = heapq.heappop_max(stones) # O(1)
            x = heapq.heappop_max(stones) # O(1)
            remaining = y - x
            if remaining:
                heapq.heappush_max(stones, remaining) # O (log n)
        if stones:
            return stones[0]
        else:
            return 0
