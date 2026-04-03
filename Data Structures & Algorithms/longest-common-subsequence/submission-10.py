class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for j in range(len(text2)+1)]

        for i in range(1, len(text1) + 1):
            dp_prev = [0]
            for j in range(1, len(text2) + 1):
                dp_prev.append(dp[j])
                if text1[i-1] == text2[j-1]:
                    dp[j] = 1 + dp_prev[-2]
                else:
                    dp[j] = max(dp[j], dp[j-1])
            print(i, dp)
        return dp[-1]
