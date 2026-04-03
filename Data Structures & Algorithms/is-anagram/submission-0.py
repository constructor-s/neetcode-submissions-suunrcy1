class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def char_counts(u):
            count = {}
            for i in u:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
            return count
        return char_counts(s) == char_counts(t)
