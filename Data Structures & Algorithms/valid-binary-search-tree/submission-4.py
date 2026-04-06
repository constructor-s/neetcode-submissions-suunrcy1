# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=float("-inf"), upper=float("inf")) -> bool:
        if not root:
            return True
        if not (lower < root.val < upper):
            return False

        if not root.left and not root.right:
            return True
        if not root.left and root.right:
            return root.val < root.right.val and self.isValidBST(root.right, lower=root.val, upper=upper)
        if root.left and not root.right:
            return root.left.val < root.val and self.isValidBST(root.left, lower=lower, upper=root.val)
        
        return root.left.val < root.val < root.right.val and self.isValidBST(root.left, lower=lower, upper=root.val) and self.isValidBST(root.right, lower=root.val, upper=upper)
