# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def is_mirror(self, node1, node2):
        if not node1 and not node2: return True
        if node1 is None or node2 is None: return False
        if node1.val != node2.val: return False
                
        return self.is_mirror(node1.left, node2.right) and self.is_mirror(node1.right, node2.left)

        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:       
        if not root: return True
        return self.is_mirror(root.left, root.right)
        
    