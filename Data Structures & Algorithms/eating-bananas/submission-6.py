import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        l = 1
        r = max(piles)
        is_solution = lambda k: sum(math.ceil(p*1.0/k) for p in piles) <= h

        res = r
        while l <= r:
            m = l + (r - l) // 2
            if is_solution(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
