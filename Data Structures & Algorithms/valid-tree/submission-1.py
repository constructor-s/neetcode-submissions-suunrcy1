from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree is a connected graph that is acyclic 
        # and has n - 1 edges for n nodes.
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # Remove any nodes that have only one edge
        while True:
            prune = set()
            for k, v in adj.items():
                if len(v) <= 1:
                    prune.add(k)

            for k in prune:
                del adj[k]

            for k, v in adj.items():
                v = [i for i in v if i not in prune]
                adj[k] = v

            if not prune:
                return not adj
