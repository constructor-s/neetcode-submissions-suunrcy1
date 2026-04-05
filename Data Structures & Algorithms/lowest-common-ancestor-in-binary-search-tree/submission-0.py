# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import *

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p

        queue = deque()
        queue.append(root)

        ancestor = None
        while queue:
            n = queue.popleft()
            if q.val < n.val: # p.val < q.val < n.val:
                if n.left:
                    queue.append(n.left)
            elif n.val < p.val: # n.val < p.val < q.val
                if n.right:
                    queue.append(n.right)
            else: # if p.val <= n.val <= q.val:
                return n
