class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pali(s: str) -> bool:
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        res = []
        stack = [(tuple(), s)]
        
        while stack:
            curr, rema = stack.pop()
            if not curr or is_pali(curr[-1]):
                if not rema:
                    res.append(list(curr))
                else:
                    for i in range(1, len(rema) + 1):
                        stack.append((
                            curr + (rema[:i], ),
                            rema[i:]
                        ))
        return res
