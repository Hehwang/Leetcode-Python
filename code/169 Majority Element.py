class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        cur=nums[0]
        for i in range(1,len(nums)):
            tmp=nums[i]
            if tmp!=cur:
                count-=1
            else:
                count+=1
            if count<0:
                count=0
                cur=tmp
        return cur