class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights); n = len(heights[0])
        pacif = [[False for j in range(n)] for i in range(m)]
        atlan = [[False for j in range(n)] for i in range(m)]

        pacif_seeds = []
        atlan_seeds = []
        
        for i in range(m):
            pacif_seeds.append((i, 0))
            atlan_seeds.append((i, n - 1))
        for j in range(n):
            pacif_seeds.append((0, j))
            atlan_seeds.append((m - 1, j))

        self.fill(heights, pacif, pacif_seeds)
        self.fill(heights, atlan, atlan_seeds)

        return [(i, j) for i in range(0, m) for j in range(0, n) if pacif[i][j] and atlan[i][j]]

    def fill(self, heights, arr, seeds):
        visited = set()
        stack = list(seeds)
        while stack:
            i, j = stack.pop()
            arr[i][j] = True
            visited.add((i, j))

            for dx, dy in (
                (-1, 0), (0, -1), (1, 0), (0, 1)
            ):
                i_ = i + dx
                j_ = j + dy
                if (i_, j_) not in visited and 0 <= i_ < len(heights) and 0 <= j_ < len(heights[0]) and heights[i_][j_] >= heights[i][j]:
                    stack.append((i_, j_))
