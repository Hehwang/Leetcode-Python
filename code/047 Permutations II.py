class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,nums,tmp,n):
        if len(tmp)==n:
            self.res.append(tmp)
        else:
            for i in range(len(nums)):
                if i<len(nums)-1 and nums[i]==nums[i+1]:
                    continue
                self.helper(nums[:i]+nums[i+1:],tmp+[nums[i]],n)
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        self.helper(nums,[],len(nums))
        return self.res