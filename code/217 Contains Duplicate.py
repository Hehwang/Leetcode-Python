class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmpset=set([])
        for i in range(len(nums)):
            if nums[i] in tmpset:
                return True
            else:
                tmpset.add(nums[i])
        return False