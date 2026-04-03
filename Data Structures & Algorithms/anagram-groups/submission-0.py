class Solution:
    @staticmethod
    def is_anagram(a, b):
        if len(a) != len(b):
            return False
        d = {}
        for i, j in zip(a, b):
            d[i] = d.get(i, 0) + 1
            d[j] = d.get(j, 0) - 1
        for k in d.values():
            if k != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for s in strs:
            for group in res:
                first = group[0]
                if self.is_anagram(first, s):
                    group.append(s)
                    break
            else:
                res.append([s])
        return res
            