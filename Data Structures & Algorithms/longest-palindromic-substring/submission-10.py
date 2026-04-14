class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (0, 0)
        # odd
        for c in range(len(s)):
            l = c
            r = c
            while 0 <= l-1 and r+1 < len(s) and s[l-1] == s[r+1]:
                l = l-1
                r = r+1
            if r - l > longest[1] - longest[0]:
                longest = (l, r)

        # even
        for c in range(len(s)-1):
            if s[c] == s[c+1]:
                l = c
                r = c + 1
                while 0 <= l-1 and r+1 < len(s) and s[l-1] == s[r+1]:
                    l = l-1
                    r = r+1
                if r - l > longest[1] - longest[0]:
                    longest = (l, r)

        return s[longest[0]:longest[1]+1]
