class Solution(object):
    def findLowIndex(self,nums,target):
        if len(nums)==0:
            return -1
        low=0
        if nums[low]==target:
            return low
        high=len(nums)-1
        while low<high-1:
            mid=int((low+high)/2)
            if nums[mid]<target:
                low=mid
            elif nums[mid]>=target:
                high=mid
        return high if nums[high]==target else -1   
    def findHighIndex(self,nums,target):
        if len(nums)==0:
            return -1
        low=0
        high=len(nums)-1
        if nums[high]==target:
            return high
        while low<high-1:
            mid=int((low+high)/2)
            if nums[mid]<=target:
                low=mid
            elif nums[mid]>target:
                high=mid
        return low if nums[low]==target else -1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findLowIndex(nums,target),self.findHighIndex(nums,target)]