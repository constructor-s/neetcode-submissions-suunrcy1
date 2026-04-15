# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preoder: top, left.top, preorder(left.left), preorder(left.right), preorder(right)
        inorder: inorder(left.left), left.top, inorder(left.right), top, inorder(right)

        we know that: values are unique
        top = preorder[0]
        -> we can find inorder(left)
        -> we can find preorder(left)
        """
        if not preorder:
            return None
                
        val = preorder[0]
        root = TreeNode(val)
        # Find index of val in inorder
        split = inorder.index(val)
        # the number of elements in the left side = split
        root.left = self.buildTree(
            preorder=preorder[1:1+split],
            inorder=inorder[0:split]
        )
        root.right = self.buildTree(
            preorder=preorder[1+split:],
            inorder=inorder[1+split:]
        )

        return root
