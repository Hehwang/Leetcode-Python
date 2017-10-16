class Solution(object):
    def helper(self,nums):
        lastmax=0
        length=len(nums)
        for i in range(length):
            if nums[i]>=nums[lastmax]:
                nums[lastmax:i]=[nums[lastmax]]*(i-lastmax)
                lastmax=i
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        import copy
        height1=copy.deepcopy(height)
        
        self.helper(height)
        height.reverse()
        self.helper(height)
        height.reverse()
        res=0
        for i in range(len(height1)):
            res+=(height[i]-height1[i])
        return res