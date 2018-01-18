class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False
        return num&(num-1)==0 and num**0.5==int(num**0.5)