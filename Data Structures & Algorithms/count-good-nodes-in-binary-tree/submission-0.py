# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Do DFS and keep track of the running max along the path
        """

        def num_good_nodes(curr, running_max=float("-inf")):
            """
            Return the number of good nodes 
            in the subtree from curr
            inclusive of curr
            """
            res = 0
            if curr.val >= running_max:
                res += 1
            
            if curr.left:
                res += num_good_nodes(curr.left, max(curr.val, running_max))
            if curr.right:
                res += num_good_nodes(curr.right, max(curr.val, running_max))

            return res
        
        return num_good_nodes(root)
