class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        while i<len(nums):
            if nums[i]!=i+1:
                tmp=nums[i]
                nums[i],nums[tmp-1]=nums[tmp-1],nums[i]
                if nums[i]==nums[nums[i]-1]:
                    i+=1
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return [nums[i],i+1]