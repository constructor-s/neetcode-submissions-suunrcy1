class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_end = [-1] * (max(i[0] for i in intervals) + 1)

        for start, end in intervals:
            max_end[start] = max(max_end[start], end)

        res = []
        curr_start = None
        curr_end = None
        for i in range(len(max_end)):
            if max_end[i] != -1:
                if curr_start is None:
                    curr_start = i
                    curr_end = max_end[i]
                else:
                    # already in an interval
                    curr_end = max(curr_end, max_end[i])

            if i == curr_end:
                print(curr_start, curr_end)
                if curr_start != -1 and curr_end != -1:
                    res.append([curr_start, curr_end])
                    curr_start = None
                    curr_end = None

        if curr_start is not None:
            res.append([curr_start, curr_end])

        return res
