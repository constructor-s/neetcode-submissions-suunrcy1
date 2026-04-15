class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        dp = [[0 for j in range(n)] for i in range(m)]
        # first column
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]
        # first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]
        
        # rest of the board
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
