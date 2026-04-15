class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        if m > n:
            m, n = n, m # gaurantee: m <= n

        dp = [1] * m # this is the first column
        for j in range(1, n):
            for i in range(1, m):
                dp[i] = dp[i-1] + dp[i]
        
        return dp[-1]
