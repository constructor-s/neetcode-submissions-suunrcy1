class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2c = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        if not digits:
            return []
        res = list(d2c[digits[0]])
        for i in range(1, len(digits)):
            res1 = []
            for r in res:
                for c in d2c[digits[i]]:
                    res1.append(r + c)
            res = res1
        return res
