# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def __init__(self):
        self.res=0
    def helper(self,path,root,target):
        count=0
        for i in range(len(path)-1):
            path[i]=path[i]+path[-1]            
            if path[i]==target:
                count+=1
        if path[-1]==target:
            count+=1
        self.res+=count
        if root.left:
            self.helper(path+[root.left.val],root.left,target)
        if root.right:
            self.helper(path+[root.right.val],root.right,target)   
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.helper([root.val],root,sum)
        return self.res
        
        