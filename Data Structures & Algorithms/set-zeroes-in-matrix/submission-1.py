class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        c0 = 1 # flag for column 0, if it is zero there is at least one zero, otherwise it is 1
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                c0 = 0
                break

        for r in range(len(matrix)):
            for v in matrix[r]:
                if v == 0:
                    matrix[r][0] = 0
                    break

        for c in range(1, len(matrix[0])):
            for r in range(len(matrix)):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    break

        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[r])):
                    matrix[r][c] = 0
        
        if c0 == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
