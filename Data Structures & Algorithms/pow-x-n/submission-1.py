class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        elif n == 0:
            return 1
        else:
            i = 1
            y = x
            cache = []
            cache.append((i, y))
            while i * 2 <= n:
                i = i * 2
                y = y * y
                cache.append((i, y))
            for j, val in reversed(cache):
                if n - i >= j:
                    y = y * val
                    i = i + j
                if i == n:
                    return y
