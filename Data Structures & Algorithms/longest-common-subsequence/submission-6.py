from functools import cache

class Solution:
    @cache
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if text1[-1] == text2[-1]:
            return 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
        return max(
            self.longestCommonSubsequence(text1[:-1], text2),
            self.longestCommonSubsequence(text1, text2[:-1])
        )
        
            