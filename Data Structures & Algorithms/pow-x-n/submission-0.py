class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = 1
        for i in range(n):
            y *= x
        for i in range(0, n, -1):
            y /= x
        return y
