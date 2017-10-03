class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        localmax=nums[0]
        localmin=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            tmp=localmax
            localmax=max(nums[i],max(nums[i]*tmp,nums[i]*localmin))
            localmin=min(nums[i],min(nums[i]*tmp,nums[i]*localmin))
            res=max(res,max(localmax,localmin))
            
        return res