class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_c=num
        lens=0
        while num_c!=0:
            lens+=1
            num_c=num_c>>1
        return (2**lens-1)^num