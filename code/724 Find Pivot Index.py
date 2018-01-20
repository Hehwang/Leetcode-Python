class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -1
        count=0
        pivot=None
        Flag=True
        left,right=0,sum(nums[1:])
        if left==right:
            count+=1
            pivot=0
            Flag=False
        for i in range(1,len(nums)):
            left+=nums[i-1]
            right-=nums[i]
            if left==right and Flag:
                count+=1
                pivot=i
                Flag=False
        return -1 if count==0 else pivot