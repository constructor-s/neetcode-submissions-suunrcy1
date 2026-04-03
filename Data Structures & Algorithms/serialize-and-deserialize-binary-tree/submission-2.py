# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        to_expand = deque([root])
        res = []
        while to_expand:
            node = to_expand.popleft()
            if node is not None:
                res.append(str(node.val))
                to_expand.append(node.left)
                to_expand.append(node.right)
            else:
                res.append("")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        data = data.split(",")
        data = deque(int(i) if i else None for i in data)

        v = data.popleft()
        root = TreeNode(v, None, None)
        
        waiting_children_queue = deque([root])
        while data:
            parent = waiting_children_queue.popleft()
            if data:
                v = data.popleft()
                if v:
                    n = TreeNode(v, None, None)
                    parent.left = n
                    waiting_children_queue.append(n)
            if data:
                v = data.popleft()
                if v:
                    n = TreeNode(v, None, None)
                    parent.right = n
                    waiting_children_queue.append(n)
        
        return root
            
