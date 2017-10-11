class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,nums,tmp,n):
        if len(tmp)==n:
            self.res.append(tmp)
        else:
            for i in range(len(nums)):
                self.helper(nums[:i]+nums[i+1:],tmp+[nums[i]],n)
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.helper(nums,[],len(nums))
        return self.res