# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        
        if p.val != q.val: return False
        
        if self.isSameTree(p.left, q.left): return (self.isSameTree(p.right, q.right))
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
    print(s.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))))
    print(s.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))))
