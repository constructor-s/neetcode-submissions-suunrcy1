class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_len = 0

        for i in range(len(s)): # left
            c = s[i]
            changes = 0
            j = i
            while j != len(s) and (s[j] == c or changes < k):
                if s[j] != c:
                    changes += 1
                j += 1
            # s[i:j] is the repeating with n=changes changes
            curr_len = min(j - i + k - changes, len(s))
            longest_len = max(curr_len, longest_len)
                
        return longest_len
