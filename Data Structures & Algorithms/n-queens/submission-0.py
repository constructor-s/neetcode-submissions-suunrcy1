EMPTY = '.'
QUEEN = 'Q'
PROHIBITED = 'X'

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [[EMPTY] * n for _ in range(n)]
        self.search(0, 0, board, res)
        return [["".join(row) for row in board] for board in res]

    def search(self, depth: int, idx: int, board: List[List[str]], res: List[List[List[str]]]) -> None:
        n = len(board); assert n == len(board[0])
        if depth == n:
            res.append([[{PROHIBITED: EMPTY}.get(i, i) for i in row] for row in board])
            return
        
        for index in range(idx, n * n):
            i = index // n
            j = index % n
            if board[i][j] == EMPTY:
                # Try to put the queen there:
                board[i][j] = QUEEN
                marks = []
                for k in range(n):
                    if board[i][k] == EMPTY:
                        marks.append((i, k))
                    if board[k][j] == EMPTY:
                        marks.append((k, j))
                    
                    # i = 1, j = 2
                    # k = 2 -> j + k - i = 2 + 2 - 1 = 3
                    #       -> j + i - k = 2 + 1 - 2 = 1
                    if 0 <= j + k - i < n and board[k][j + k - i] == EMPTY:
                        marks.append((k, j + k - i))
                    if 0 <= j + i - k < n and board[k][j + i - k] == EMPTY:
                        marks.append((k, j + i - k))
                for y, x in marks:
                    board[y][x] = PROHIBITED

                self.search(depth + 1, index, board, res)

                # Revert to previous state
                for y, x in marks:
                    board[y][x] = EMPTY
                board[i][j] = EMPTY
