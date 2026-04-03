from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        PAIRS = (
            "()",
            "{}",
            "[]"
        )
        stack = deque()
        for c in s:
            for open_char, close_char in PAIRS:
                if c == open_char:
                    stack.append(c)
                elif c == close_char:
                    if stack and stack[-1] == open_char:
                        stack.pop()
                    else:
                        return False
        return not stack
