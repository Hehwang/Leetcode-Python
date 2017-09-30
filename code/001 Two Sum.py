class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict={}
        for i in range(len(nums)):
            tmp=target-nums[i]
            if tmp in numsDict:
                return [i,numsDict[tmp]]
            numsDict[nums[i]]=i