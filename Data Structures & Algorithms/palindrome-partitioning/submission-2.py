class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False for l in range(r+1)] for r in range(len(s))]
        for r in range(len(s)):
            for l in range(r+1):
                if (l == r or 
                    (s[l] == s[r] and r - l <= 2) or 
                    (s[l] == s[r] and dp[r-1][l+1])):
                    dp[r][l] = True
        
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
