# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res=[]
        queue=[root]
        while len(queue)>0:
            row=[]
            queue2=[]
            for node in queue:
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
                row.append(node.val)
            res.append(max(row))
            queue=queue2
        return res
        