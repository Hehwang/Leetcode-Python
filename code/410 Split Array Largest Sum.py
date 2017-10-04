class Solution(object):
    def splitArrayhelper(self,nums,k,m):
        tmpsum=0
        for i in range(len(nums)):
            tmpsum+=nums[i]
            if tmpsum>k:
                tmpsum=nums[i]
                m-=1
            if m==0:
                return False
        return True

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        low=max(nums)
        high=sum(nums)
        while low<high:
            mid=(low+high)//2
            if self.splitArrayhelper(nums,mid,m):
                high=mid-1
            else:
                low=mid+1
        if self.splitArrayhelper(nums,low,m):
            return low
        else:
            return low+1