class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones,twos = 0,0
        for i in range(len(nums)):
            twos|=ones & nums[i]
            ones=ones^nums[i]
            three=ones & twos
            ones&=~three
            twos&=~three
        return ones