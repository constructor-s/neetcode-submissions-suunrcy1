class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str, l: int, r: int):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        dp = [[is_palindrome(s, l, r) for l in range(r+1)] for r in range(len(s))]
        # print(dp)

        res = []
        stack = [(0, [])]
        while stack:
            l, path = stack.pop()
            if l == len(s):
                res.append(path)
            else:
                for r in range(l, len(s)):
                    if dp[r][l]:
                        stack.append((r + 1, path + [s[l:r + 1]]))
        return res
