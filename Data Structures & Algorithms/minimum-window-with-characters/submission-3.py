class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # len(s) >= len(t)
        # Get dict that has counts of t
        counts = {}
        for c in t:
            counts[c] = counts.get(c, 0) + 1

        i = 0
        j = -1
        shortest = ""
        while i < len(s) and j < len(s): # TODO
            # print(i, j, counts)
            if all(i <= 0 for i in counts.values()):
                # This is a match
                if not shortest or j + 1 - i < len(shortest):
                    shortest = s[i:j+1]

                # Remove the left
                c = s[i]
                counts[c] += 1
                i += 1
            else:
                j += 1
                if j == len(s):
                    break
                c = s[j]
                counts[c] = counts.get(c, 0) - 1

        return shortest

