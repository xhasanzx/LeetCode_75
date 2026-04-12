from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        
        res = []
        
        # Left
        res += self.inorderTraversal(root.left)
        
        # Root
        res.append(root.val)
        
        # Right
        res += self.inorderTraversal(root.right)
        
        return res




if __name__ == "__main__":
    solution = Solution()
    input_tree = TreeNode(1, TreeNode(4, None, None), TreeNode(2, TreeNode(3), None))
    print(solution.inorderTraversal(input_tree))     
