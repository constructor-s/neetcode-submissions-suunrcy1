class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(board: List[List[str]], word: str, i: int, j: int) -> bool:
            if not word:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[0]:
                return False

            c = board[i][j]
            board[i][j] = "*"
            if search(board, word[1:], i-1, j):
                return True
            if search(board, word[1:], i+1, j):
                return True
            if search(board, word[1:], i, j-1):
                return True
            if search(board, word[1:], i, j+1):
                return True
            board[i][j] = c
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(board, word, i, j):
                    return True

        return False
