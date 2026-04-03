class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        for ss, tt in zip(s, t):
            d[ss] = d.get(ss, 0) + 1
            d[tt] = d.get(tt, 0) - 1
        
        for v in d.values():
            if v:
                return False
        return True
