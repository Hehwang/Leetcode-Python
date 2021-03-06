# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,total,root,path,sum):
        if not (root.right or root.left):
            if total+root.val==sum:
                self.res.append(path+[root.val])
        else:
            for i in range(2):
                if i==0 and root.left:
                    self.helper(total+root.val,root.left,path+[root.val],sum)
                elif i==1 and root.right:
                    self.helper(total+root.val,root.right,path+[root.val],sum)
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root:
            path=[]
            self.helper(0,root,path,sum)
        return self.res