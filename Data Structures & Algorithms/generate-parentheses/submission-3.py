class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = [[] for i in range(n + 1)]
        results[0] = [""]
        for i in range(1, n + 1):
            for l in range(i): # 0 to i-1
                r = i - l - 1 # i-1 to 0
                
                for left in results[l]:
                    for right in results[r]:
                        results[i].append("(" + left + ")" + right)

        return results[n]
