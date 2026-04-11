from collections import defaultdict
from bisect import insort

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for fr, to in tickets:
            insort(adj[fr], to)
        print(adj)

        path = []
        stack = ["JFK"]
        while stack:
            fr = stack[-1]
            if adj[fr]:
                to = adj[fr].pop(0)
                stack.append(to)
            else:
                stack.pop()
                path.append(fr)

        return path[::-1]
