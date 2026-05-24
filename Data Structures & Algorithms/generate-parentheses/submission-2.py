from functools import cache

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        res = []
        stack = [("(", 1, 0)]
        while stack:
            s, l, r = stack.pop()
            assert len(s) == l + r
            if l == r == n:
                res.append(s)
            elif len(s) < 2 * n and l >= r: # left brackets must be >= right brackets
                stack.append((s + "(", l + 1, r))
                stack.append((s + ")", l, r + 1))

        return res
