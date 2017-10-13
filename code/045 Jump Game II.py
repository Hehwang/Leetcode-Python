class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        start=0
        end=nums[0]
        maxRight=nums[0]
        step=1
        
        while end<len(nums)-1:
            for j in range(start+1,end+1):
                maxRight=max(maxRight,j+nums[j])
            start=end
            end=maxRight
            step+=1
        return step