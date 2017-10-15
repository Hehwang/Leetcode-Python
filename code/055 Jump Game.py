class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
		##O(n)
        maxRight=0
        i=0
        while maxRight<len(nums)-1:
            maxRight=max(maxRight,nums[i]+i)
            if maxRight<=i:
                return False
            i+=1
        return True