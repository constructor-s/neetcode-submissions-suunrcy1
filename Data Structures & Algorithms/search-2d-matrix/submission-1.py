class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if target < matrix[0][0]:
            return False
        if target > matrix[-1][-1]:
            return False
        
        def to_2d(x, matrix):
            m, n = len(matrix), len(matrix[0])
            return x // n, x % n
        def to_1d(i, j, matrix):
            m, n = len(matrix), len(matrix[0])
            return n * i + j
        def get(x, matrix):
            i, j = to_2d(x, matrix)
            return matrix[i][j]
        
        # binary search
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            m = l + (r - l) // 2
            print(l, m, r, get(l, matrix), get(m, matrix), get(r, matrix))
            if target < get(m, matrix):
                r = m - 1
            else:
                l = m + 1
        # print(l, m, r, get(l, matrix), get(m, matrix), get(r, matrix))
        return get(r, matrix) == target
