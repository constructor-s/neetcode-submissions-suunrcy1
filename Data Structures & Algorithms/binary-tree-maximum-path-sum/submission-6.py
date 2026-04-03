# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Test case:
       -15
  10          20
            15   5
           -5 -6
"""

def dfs(n: TreeNode):
    """
    Returns: 
    """
    left_chain_sum = dfs(n.left)[0] if n.left else 0
    right_chain_sum = dfs(n.right)[0] if n.right else 0
    left_path_sum = dfs(n.left)[1] if n.left else 0
    right_path_sum = dfs(n.right)[1] if n.right else 0
    # The new best chain sum is the maximum of left 
    # chain and right chain plus current val which
    # must be added to the chain
    new_chain_sum = max([0, left_chain_sum, right_chain_sum]) + n.val

    # The new best path is either:
    # - the left path
    # - the right path
    # - the left chain if > 0 + n.val + the right chain if > 0
    new_path_sum = max([
        left_path_sum if n.left else float("-inf"),
        right_path_sum if n.right else float("-inf"),
        max(left_chain_sum, 0) + n.val + max(right_chain_sum, 0)
    ])

    return new_chain_sum, new_path_sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        chain_sum, path_sum = dfs(root)
        print(chain_sum, path_sum)
        return path_sum

