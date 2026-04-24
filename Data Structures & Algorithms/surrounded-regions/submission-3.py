from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    # BFS
                    visited = set()
                    q = deque()
                    q.append((i, j))

                    while q:
                        y, x = q.popleft()
                        if (y, x) in visited:
                            continue
                        if 0 <= y < len(board) and 0 <= x < len(board[0]):
                            if board[y][x] == "O":
                                visited.add((y, x))
                                q.append((y - 1, x))
                                q.append((y + 1, x))
                                q.append((y, x - 1))
                                q.append((y, x + 1))
                        else:
                            q.append((y, x))
                            break # hit the border

                    if not q: # did not hit the border - fill it in
                        for y, x in visited:
                            board[y][x] = "X"
