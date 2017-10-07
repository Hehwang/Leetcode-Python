class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        localsum=sum(nums[:k])
        globalsum=sum(nums[:k])
        for i in range(k,len(nums)):
            localsum+=nums[i]-nums[i-k]
            globalsum=max(globalsum,localsum)
        return float(globalsum)/float(k)