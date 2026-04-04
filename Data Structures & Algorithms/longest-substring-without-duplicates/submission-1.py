class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set()
        i = 0
        max_len = 0
        for j in range(0, len(s)):
            while s[j] in char_set:
                # remove from left
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])
            max_len = len(char_set) if len(char_set) > max_len else max_len
        
        return max_len
