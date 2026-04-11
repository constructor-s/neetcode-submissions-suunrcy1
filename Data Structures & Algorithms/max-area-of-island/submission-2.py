from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(grid, r, c):
            q = deque()
            q.append((r, c))
            area = 0
            while q:
                r, c = q.popleft()
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == 1:
                    area += 1
                    grid[r][c] = 2 # mark visited
                    q.append((r-1, c))
                    q.append((r+1, c))
                    q.append((r, c-1))
                    q.append((r, c+1))
            return area

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                area = search(grid, r, c)
                if max_area < area:
                    max_area = area
        return max_area

        """
       [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        """