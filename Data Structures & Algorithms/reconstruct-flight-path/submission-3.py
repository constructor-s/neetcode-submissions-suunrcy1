from collections import defaultdict
from bisect import insort

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def insort_descending(a, x):
            lo = 0
            hi = len(a) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if a[mid] > x:
                    lo = mid + 1
                else:
                    hi = mid - 1
            a.insert(lo, x)

        adj = defaultdict(list)
        for fr, to in tickets:
            insort_descending(adj[fr], to)

        path = []
        stack = ["JFK"]
        while stack:
            fr = stack[-1]
            if adj[fr]:
                to = adj[fr].pop()
                stack.append(to)
            else:
                stack.pop()
                path.append(fr)

        return path[::-1]
