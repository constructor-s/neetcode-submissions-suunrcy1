class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains_every_char(source, test):
            d = {}
            for c in test:
                d[c] = d.get(c, 0) + 1
            for c in source:
                d[c] = d.get(c, 0) - 1
            for v in d.values():
                if v > 0:
                    return False
            return True

        best = ""
        l = 0
        r = 0
        while l < len(s) and r <= len(s):
            if contains_every_char(s[l:r], t):
                new_substr = s[l:r]
                if not best or len(new_substr) < len(best):
                    best = new_substr
                l += 1
            else:
                r += 1
        return best
