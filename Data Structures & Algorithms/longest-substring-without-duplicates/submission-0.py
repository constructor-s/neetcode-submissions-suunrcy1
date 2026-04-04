class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i = 0
        j = 1
        max_len = 0
        while i < len(s) and j <= len(s):
            if len(set(s[i:j])) == j - i:
                max_len = max(max_len, j - i)
                j += 1
            else:
                i += 1
        return max_len
