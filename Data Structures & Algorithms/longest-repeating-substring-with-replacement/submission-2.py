class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def changes_needed(counts):
            if not counts:
                return 0
            arg_max = max(counts, key=lambda x: counts[x])
            return sum(counts.values()) - counts[arg_max]

        counts = {}

        i = 0
        j = 0

        max_len = 0
        while i <= len(s) and j <= len(s):
            if changes_needed(counts) <= k:
                max_len = max(max_len, j - i)
                if j < len(s):
                    counts[s[j]] = counts.get(s[j], 0) + 1
                j += 1
            else:
                counts[s[i]] -= 1
                i += 1

        return max_len
