import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h) # O(k)
        for i in range(k, len(nums)):
            heapq.heappushpop(h, nums[i]) # O(n log k)
        return heapq.heappop(h) # O(log k)
