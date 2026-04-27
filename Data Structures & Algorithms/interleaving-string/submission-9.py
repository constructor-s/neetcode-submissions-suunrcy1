class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        """
        k = i + j
        if k == len(s3):
            return True

        if i < len(s1) and s1[i] == s3[k] and self.isInterleave(s1, s2, s3, i+1, j):
            return True

        if j < len(s2) and s2[j] == s3[k] and self.isInterleave(s1, s2, s3, i, j+1):
            return True
        
        return False
        """

        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        # Can s1[:i] and s2[:j] form s3[:i+j]?
        dp[0][0] = True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                k = i + j
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j-1] and s2[j-1] == s3[k-1])
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[k-1])
        return dp[-1][-1]
