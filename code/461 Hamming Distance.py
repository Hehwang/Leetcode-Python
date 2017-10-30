class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp=x^y
        res=0
        while tmp!=0:
            if tmp%2!=0:
                res+=1
            tmp=tmp>>1
        return res