class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(r):
            r = [i for i in r if i != "."]
            return len(set(r)) == len(r)
        
        for row in board:
            if not isValidRow(row):
                return False

        for j in range(len(board[0])):
            col = [row[j] for row in board]
            if not isValidRow(col):
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                box = [board[i][j], board[i][j+1], board[i][j+2],
                       board[i+1][j], board[i+1][j+1], board[i+1][j+2],
                       board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
                if not isValidRow(box):
                    return False

        return True
