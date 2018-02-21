# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,root):
        if root:
            tmp=root.right
            root.right=root.left
            root.left=tmp
            self.helper(root.right)
            self.helper(root.left)
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.helper(root)
        return root