class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for j in range(len(text2)+1)]

        for i in range(1, len(text1) + 1):
            dp_prev = 0
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    temp = 1 + dp_prev
                    dp_prev = dp[j]
                    dp[j] = temp
                else:
                    temp = max(dp[j], dp[j-1])
                    dp_prev = dp[j]
                    dp[j] = temp
            print(i, dp)
        return dp[-1]
