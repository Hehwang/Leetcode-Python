# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        else:
            tmp=max(nums)
            tmpindex=nums.index(tmp)
            res=TreeNode(tmp)
            res.left=self.constructMaximumBinaryTree(nums[:tmpindex])
            res.right=self.constructMaximumBinaryTree(nums[tmpindex+1:])
            return res