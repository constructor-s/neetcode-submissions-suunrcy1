class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals:
            return [-1 for _ in queries]

        t_max = max(right for _, right in intervals)

        lengths = [float("inf") for _ in range(t_max+1)]
        for left, right in intervals:
            for i in range(left, right+1):
                lengths[i] = min(lengths[i], right - left + 1)

        res = []
        for i in queries:
            if i >= len(lengths):
                res.append(-1)
            elif lengths[i] == float("inf"):
                res.append(-1)
            else:
                res.append(lengths[i])

        return res
