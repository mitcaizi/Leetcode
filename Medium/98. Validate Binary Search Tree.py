# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.BST(root, float('-inf'), float('inf'))
        def BST(self, root, min, max):
            if not root:
                return True
            if root.val >= max or root.val <= min:
                return False
            return self.BST(root.left, min, root.val) and self.BST(root.right, root.val, max)