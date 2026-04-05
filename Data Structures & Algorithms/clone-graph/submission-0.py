"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.nodes = {} # maps val to node, cache

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node.val in self.nodes:
            return self.nodes[node.val]

        # Copy the nodes
        root = Node(val=node.val, neighbors=None)
        self.nodes[node.val] = root
        root.neighbors = [
            self.cloneGraph(n) for n in node.neighbors
        ]
        return root
