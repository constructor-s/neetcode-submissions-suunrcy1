# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do DFS, collect in order
        collected = []

        def dfs(node: TreeNode):
            if len(collected) >= k:
                return

            if node.left:
                dfs(node.left)
            collected.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        return collected[k-1]
