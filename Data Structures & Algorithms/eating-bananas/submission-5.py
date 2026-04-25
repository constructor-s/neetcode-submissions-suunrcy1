import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        l = 1
        r = max(piles)
        is_solution = lambda k: sum(math.ceil(p*1.0/k) for p in piles) <= h
        while l < r:
            if is_solution(l):
                return l
            m = l + (r - l) // 2
            if is_solution(m):
                r = m # r is gauranteed to be a solution after loop
            else:
                l = m + 1 # m is gaurentted to not be a solution, but if m+1 is a solution, it must be the best solution
        return r
