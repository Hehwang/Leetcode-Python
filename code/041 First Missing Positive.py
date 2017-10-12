class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]>0 and nums[i]<=len(nums) and nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                tmp=nums[i]
                nums[i],nums[tmp-1]=nums[tmp-1],nums[i]
            else:
                i+=1
        print(nums)
        i=1    
        while i<len(nums)+1:
            if nums[i-1]==i:
                i+=1
            else:
                break
        return i