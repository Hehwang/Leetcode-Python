class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        if len(nums)==1:
            return 0 if nums[0]<=target else 1 
        while low<high:
            mid=int((low+high)/2)
            if nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid
            else:
                return mid
        return low