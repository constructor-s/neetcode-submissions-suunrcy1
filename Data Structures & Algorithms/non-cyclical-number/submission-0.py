class Solution:
    def isHappy(self, n: int, seen: Optional[Set]=None) -> bool:
        if n == 1:
            return True

        if seen is None:
            seen = set()

        if n in seen:
            return False
        
        seen.add(n)

        s = 0
        while n:
            s += (n % 10) ** 2
            n //= 10

        return self.isHappy(s, seen=seen)
