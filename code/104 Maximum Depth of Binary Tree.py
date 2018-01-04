# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        if not root.right:
            return 1+self.maxDepth(root.left)
        if not root.left:
            return 1+self.maxDepth(root.right)
        return 1+max(self.maxDepth(root.right),self.maxDepth(root.left))