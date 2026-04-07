class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if newInterval[0] < intervals[0][0]:
            idx = 0
        elif newInterval[0] > intervals[-1][0]:
            idx = len(intervals)
        else:

            # Find the correct place to insert
            l = 0
            r = len(intervals) - 1
            while l < r - 1:
                m = (l + r) // 2
                if newInterval[0] <= intervals[m][0]:
                    r = m
                else:
                    l = m
            idx = l + 1
        
        intervals = intervals.copy()
        intervals.insert(idx, newInterval)
        
        i = idx
        while i - 1 >= 0 and intervals[i-1][1] >= intervals[idx][0]:
            i -= 1
        
        j = idx
        while j + 1 < len(intervals) and intervals[j+1][0] <= intervals[idx][1]:
            j += 1
        
        # replace intervals[i:j]
        intervals[i:j+1] = [[intervals[i][0], max(
            inter[1] for inter in intervals[i:j+1]
        )]]

        return intervals
