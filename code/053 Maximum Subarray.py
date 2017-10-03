class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        localmax=nums[0]
        globalmax=nums[0]
        for i in range(1,len(nums)):
            localmax=max(nums[i],localmax+nums[i])
            globalmax=max(globalmax,localmax)
        return globalmax