# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res=[]
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            if root.left:
                self.inorderTraversal(root.left)
            self.res.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)
        return self.res
            