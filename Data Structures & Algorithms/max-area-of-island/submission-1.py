class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search(grid, r, c):
            if grid[r][c] != 1:
                return 0

            assert grid[r][c] == 1
            area = 1
            grid[r][c] = "*"
            
            if r >= 1:
                area += search(grid, r-1, c)
            if c >= 1:
                area += search(grid, r, c-1)
            if r < len(grid) - 1:
                area += search(grid, r+1, c)
            if c < len(grid[r]) - 1:
                area += search(grid, r, c+1)
            # grid[r][c] = 1

            return area

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                max_area = max(max_area, search(grid, r, c))

        return max_area
