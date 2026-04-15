import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if not tasks:
            return 0

        tasks_count = {}
        for t in tasks:
            tasks_count[t] = tasks_count.get(t, 0) + 1
        
        h = [(count, t) for t, count in tasks_count.items()]
        heapq.heapify_max(h)

        time = 0
        q = deque()
        while h or q:
            # print(h, q)
            if q and time >= q[0][2]:
                count, t, _ = q.popleft()
                count, t = heapq.heappushpop_max(h, (count, t))
                if count > 1:
                    q.append((count-1, t, time+n+1))
            elif h:
                count, t = heapq.heappop_max(h)
                if count > 1:
                    q.append((count-1, t, time+n+1))
            
            time += 1
        return time
