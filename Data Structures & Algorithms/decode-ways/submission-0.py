class Solution:
    def numDecodings(self, s: str) -> int:
        # numDecodings(s[:i+1]) = 
        # numDecodings(s[:i]) - if s[i] is not '0'
        # + numDecodings(s[:i-1]) + 1 - if s[i-1:i+1] is valid
        # In fact, we only need to keep track of these two rather 
        # than the full dp
        
        dp0 = 1
        dp1 = 1 if s[0] != '0' else 0

        if len(s) == 0:
            return dp0
        if len(s) == 1:
            return dp1
        
        for i in range(1, len(s)):
            dp2 = 0
            if s[i] != '0':
                dp2 += dp1
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp2 += dp0
            dp0, dp1 = dp1, dp2

        return dp1
