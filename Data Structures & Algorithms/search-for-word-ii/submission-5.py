class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a trie using just dict
        # refs is impelemented for pruning
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {"refs": 1}
                else:
                    curr[c]["refs"] += 1
                curr = curr[c]
            curr["word"] = word

        def search(board, r, c, root):
            """Recursively DFS the board, collect words reached."""
            if not board or r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return []
            if board[r][c] not in root or root[board[r][c]]["refs"] == 0:
                return []

            # board[r][c] is a possible path
            result = []
            if "word" in root[board[r][c]]:
                result.append(root[board[r][c]]["word"])
            
            curr_char = board[r][c]
            board[r][c] = ""
            result.extend(search(board, r-1, c, root[curr_char]))
            result.extend(search(board, r+1, c, root[curr_char]))
            result.extend(search(board, r, c-1, root[curr_char]))
            result.extend(search(board, r, c+1, root[curr_char]))
            
            board[r][c] = curr_char
            root[board[r][c]]["refs"] -= len(result)

            return result
        
        # Start search from any cell on the board
        result = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                result.update(search(board, r, c, root))
        return list(result)
