# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.flag=True
    
    def helper(self,root,max_num,min_num):
        if root.left:
            if root.left.val<=min_num or root.left.val>=max_num or root.left.val>=root.val:
                self.flag=False
            self.helper(root.left,min(max_num,root.val),min_num)
        if root.right:
            if root.right.val<=min_num or root.right.val>=max_num or root.right.val<=root.val:
                self.flag=False
            self.helper(root.right,max_num,max(min_num,root.val))
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        max_num=2**32
        min_num=-2**32
        self.helper(root,max_num,min_num)
        return self.flag