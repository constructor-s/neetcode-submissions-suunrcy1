# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        
        result = [[root.val]]
        while left and right:
            result.append(left.pop(0) + right.pop(0))
        if left:
            result.extend(left)
        if right:
            result.extend(right)
        return result
