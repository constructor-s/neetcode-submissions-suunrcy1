class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        spans = {}
        for i, c in enumerate(s):
            if c not in spans:
                spans[c] = [i, i+1]
            else:
                spans[c][1] = i+1
        
        spans = sorted(spans.items(), key=lambda x: x[1])
        print(spans)

        res = []
        while spans:
            _, (start, end) = spans.pop(0)
            if not res or start >= res[-1]:
                res.append(end)
            else:
                res[-1] = max(res[-1], end)
        
        diff = [res[0]]
        for i in range(1, len(res)):
            diff.append(res[i] - res[i-1])
        return diff
