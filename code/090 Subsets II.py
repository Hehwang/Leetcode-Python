class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        nums=sorted(nums)
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                lastlengh=len(res)
                res+=[x+[nums[i]] for x in res]
            elif nums[i]==nums[i-1]:
                res+=[x+[nums[i]] for x in res[-lastlengh:]]
        return res