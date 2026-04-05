class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    # Start exploring island
                    stack = [(i, j)]
                    while stack:
                        y, x = stack.pop(-1)
                        if 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] == "1":
                            grid[y][x] = "*"
                            stack.append((y-1, x))
                            stack.append((y+1, x))
                            stack.append((y, x-1))
                            stack.append((y, x+1))
        
        return islands
