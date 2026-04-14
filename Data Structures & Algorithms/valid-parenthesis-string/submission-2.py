class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            elif c == ")":
                if left:
                    left.pop(-1)
                elif star:
                    star.pop(-1)
                else:
                    return False

        # print(left)
        # print(star)
        while left:
            if not star:
                return False
            l = left.pop(-1)
            s = star.pop(-1)
            if l > s:
                return False
        return not left
