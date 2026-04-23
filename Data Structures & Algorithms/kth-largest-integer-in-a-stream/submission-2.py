import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.minh = nums[:k]
        heapq.heapify(self.minh)

    def add(self, val: int) -> int:
        if len(self.minh) < self.k:
            heapq.heappush(self.minh, val)
        else:
            heapq.heappushpop(self.minh, val)
        return self.minh[0]
