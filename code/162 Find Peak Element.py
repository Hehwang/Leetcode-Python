class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return nums.index(max(nums))
        
        def helper(nums,i,j):
            m=int((i+j)/2)
            if i==j and (i==0 or i==len(nums)-1):
                return m
            if nums[m]>nums[m-1] and nums[m]>nums[m+1]:
                return m
            elif nums[m]<nums[m-1]:
                return helper(nums,i,m-1)
            elif nums[m]<nums[m+1]:
                return helper(nums,m+1,j)
        return helper(nums,0,len(nums)-1)