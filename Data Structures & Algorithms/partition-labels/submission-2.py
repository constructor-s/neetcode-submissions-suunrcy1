class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        indices = []
        for i, c in enumerate(s):
            if not indices or i > indices[-1]:
                indices.append(last_index[c])
            elif last_index[c] > indices[-1]:
                indices[-1] = last_index[c]

        res = [indices[0] + 1]
        for i in range(1, len(indices)):
            res.append(indices[i] - indices[i-1])

        return res
