class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1) # dp[i] is the number of ways to climb to stair i
                            # dp[0] = 1, dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
