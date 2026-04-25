from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)

        # Find the cycle
        # by DFS

        stack = [[1]]

        while stack:
            path = stack.pop()
            if len(path) > 1 and path[-1] in path[:-1]:
                break # found the cycle
            for bi in adj[path[-1]]:
                if len(path) == 1 or bi != path[-2]:
                    stack.append(path + [bi])

        cycle_i = path.index(path[-1])
        path = path[cycle_i:]
        for ai, bi in reversed(edges):
            if ai in path and bi in path:
                return [ai, bi]
