class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[0])

        res = 0
        curr_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < curr_end:
                # "Remove" the one that ends later
                if end < curr_end:
                    curr_end = end
                res += 1
            else:
                curr_end = end
        
        return res
