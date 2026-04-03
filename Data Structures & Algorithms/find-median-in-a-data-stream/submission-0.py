from heapq import *

class MedianFinder:
    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap
        
    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            # Maintain left one larger than right
            heappush_max(self.left, heappushpop(self.right, num))
        else:
            heappush(self.right, heappushpop_max(self.left, num))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return 0.5 * (self.left[0] + self.right[0])
        else:
            return self.left[0]
        
        