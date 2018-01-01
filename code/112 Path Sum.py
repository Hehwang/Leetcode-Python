# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res=False
    def helper(self,total,root,sum):
        if not (root.right or root.left):
            if total+root.val==sum:
                self.res=True
        else:
            for i in range(2):
                if i==0 and root.left:
                    self.helper(total+root.val,root.left,sum)
                elif i==1 and root.right:
                    self.helper(total+root.val,root.right,sum)
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root: 
            self.helper(0,root,sum)
            return self.res
        else:
            return False