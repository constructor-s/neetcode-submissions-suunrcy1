class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        q = deque()
        
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        curr_dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if 0 <= r < m and 0 <= c < n and grid[r][c] >= curr_dist: # this also gaurantees that grid[r][c] > 0
                    grid[r][c] = curr_dist
                    q.append((r-1, c))
                    q.append((r+1, c))
                    q.append((r, c-1))
                    q.append((r, c+1))
            curr_dist += 1
