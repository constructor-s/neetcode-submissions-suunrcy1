class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # (0, +1) x n - 1
        # (+1, 0) x m - 1
        # (0, -1) x n - 1
        # (-1, 0) x m - 2
        # spiral inside

        if not matrix or not matrix[0]:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [i[0] for i in matrix]
        
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        res = [matrix[0][0]]
        for k in range(n - 1):
            j += 1
            res.append(matrix[i][j])
        for k in range(m - 1):
            i += 1
            res.append(matrix[i][j])
        for k in range(n - 1):
            j -= 1
            res.append(matrix[i][j])
        for k in range(m - 2):
            i -= 1
            res.append(matrix[i][j])

        res.extend(self.spiralOrder([
            i[1:-1] for i in matrix[1:-1]
        ]))

        return res
