# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        def is_valid(root, lower, upper):
            if not root:
                return True
            if root.val > lower and root.val < upper:
                return is_valid(root.left, lower, root.val) and is_valid(root.right, root.val, upper)
            return False
        return is_valid(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST(root))  # Output: True

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(7)
    print(Solution().isValidBST(root))  # Output: False

    root = TreeNode(2)
    root.left = TreeNode(2)
    print(Solution().isValidBST(root))  # Output: False





