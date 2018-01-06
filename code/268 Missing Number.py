class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[-1]+nums
        i=1
        while i<len(nums):
            if nums[i]<0:
                i+=1
                continue
            if nums[i]!=i:
                tmp=nums[i]
                nums[i],nums[tmp]=nums[tmp],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]<0:
                return i