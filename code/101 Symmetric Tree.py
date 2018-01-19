# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,l,r):
        if not l and not r:
            return True
        elif l and r:
            return l.val==r.val and self.helper(l.left,r.right) and self.helper(l.right,r.left)
        else:
            return False
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left,root.right)