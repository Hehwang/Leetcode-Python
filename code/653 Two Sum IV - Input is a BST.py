# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.l=[]
    def helper(self,root):
        if root:
            self.l.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.helper(root)
        tmpset=set([])
        tmplist=self.l
        for i in range(len(tmplist)):
            if tmplist[i] in tmpset:
                return True
            else:
                tmpset.add(k-tmplist[i])
        return False