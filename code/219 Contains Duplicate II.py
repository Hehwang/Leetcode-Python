class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmpdict={}
        for i in range(len(nums)):
            if not(nums[i] in tmpdict):
                tmpdict[nums[i]]=i
            elif i-tmpdict[nums[i]]<=k:
                return True
            else:
                tmpdict[nums[i]]=i
        return False