# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l=[root]
        depth=0
        flag=1
        while True:
            depth+=1
            l_new=[]
            for i in l:
                if not i.right and not i.left:
                    flag=0
                if i.right:
                    l_new.append(i.right)
                if i.left:
                    l_new.append(i.left)
            if flag==0:
                break
            l=l_new
        return depth