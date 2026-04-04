class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        i = 0
        j = 0

        max_len = 0
        max_freq = 0
        while i < len(s) and j <= len(s):
            print(s[i:j], counts, max_freq)
            # counts keep track of counts of characters in s[i:j]
            if j - i - max_freq <= k:
                max_len = max(max_len, j - i)
                # Move right pointer right
                if j < len(s):
                    counts[s[j]] = counts.get(s[j], 0) + 1
                    max_freq = max(max_freq, counts[s[j]])
                j += 1
            else:
                # Move left pointer right
                counts[s[i]] -= 1
                i += 1

        return max_len
