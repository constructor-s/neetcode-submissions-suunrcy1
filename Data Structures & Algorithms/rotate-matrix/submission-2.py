class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(len(matrix) // 2):
            size = len(matrix) - i - i

            # store top edge
            top_edge = matrix[i].copy()

            for x in range(1, size):
                # top row = left column
                matrix[i][i + x] = matrix[n - 1 - i - x][i]
            for y in range(0, size - 1):
                # left column = bottom row
                matrix[i + y][i] = matrix[n - 1 - i][i + y]
            for x in range(0, size - 1):
                # bottom row = right column
                matrix[n - 1 - i][i + x] = matrix[n - 1 - i - x][n - 1 - i]
            for y in range(1, size):
                # right column = top row
                matrix[i + y][n - 1 - i] = top_edge[y + i]


