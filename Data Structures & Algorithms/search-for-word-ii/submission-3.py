class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a trie using just dict
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["word"] = word

        def search(board, r, c, root, visited):
            """Recursively DFS the board, collect words reached."""
            if not board or (r, c) in visited or r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return []
            if board[r][c] not in root:
                return []

            # board[r][c] is a possible path
            visited = set(visited)
            visited.add((r, c))

            result = []
            if "word" in root[board[r][c]]:
                result.append(root[board[r][c]]["word"])
            result.extend(search(board, r-1, c, root[board[r][c]], visited))
            result.extend(search(board, r+1, c, root[board[r][c]], visited))
            result.extend(search(board, r, c-1, root[board[r][c]], visited))
            result.extend(search(board, r, c+1, root[board[r][c]], visited))

            return result
        
        # Start search from any cell on the board
        result = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                result.update(search(board, r, c, root, {}))
        return list(result)
