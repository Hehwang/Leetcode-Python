class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor,a,b=0,0,0
        for num in nums:
            xor^=num
        mask=1
        while mask&xor==0:
            mask=mask<<1
        for num in nums:
            if num&mask:
                a^=num
            else:
                b^=num
        return [a,b]