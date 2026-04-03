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
    Returns: a tuple containing: (
        The best sum that is a single chain that can be continued, must including the current node n
        The best sum in the (sub)tree starting from n
    )
    """
    if n is None:
        return float("-inf"), float("-inf")

    left = dfs(n.left)
    right = dfs(n.right)
    left_chain_sum = left[0]
    right_chain_sum = right[0]
    left_path_sum = left[1]
    right_path_sum = right[1]
    # The new best chain sum is the maximum of left 
    # chain and right chain plus current val which
    # must be added to the chain
    new_chain_sum = max([0, left_chain_sum, right_chain_sum]) + n.val

    # The new best path is either:
    # - the left path
    # - the right path
    # - the left chain if > 0 + n.val + the right chain if > 0
    new_path_sum = max([
        left_path_sum,
        right_path_sum,
        max(left_chain_sum, 0) + n.val + max(right_chain_sum, 0)
    ])

    return new_chain_sum, new_path_sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        chain_sum, path_sum = dfs(root)
        # print(chain_sum, path_sum)
        return path_sum

