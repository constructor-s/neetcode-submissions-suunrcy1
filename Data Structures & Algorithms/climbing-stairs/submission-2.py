class Solution:
    def climbStairs(self, n: int) -> int:
        ways1 = 1
        ways2 = 2
        if n == 0:
            return 1
        if n == 1:
            return ways1
        if n == 2:
            return ways2
        for i in range(3, n+1):
            ways = ways1 + ways2
            ways1 = ways2
            ways2 = ways
        return ways
