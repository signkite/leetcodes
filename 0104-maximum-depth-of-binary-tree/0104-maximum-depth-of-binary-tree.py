# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # empty tree
        if not root:
            return 0
        
        dq = deque([(root, 1)])
        max_depth = 0
        while dq:
            node, depth = dq.popleft()
            
            if depth > max_depth:
                max_depth = depth
            
            if node.left is not None:
                dq.append((node.left, depth + 1))
                
            if node.right is not None:
                dq.append((node.right, depth + 1))
        
        return max_depth