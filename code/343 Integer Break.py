class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        if n==3:
            return 2
        a=n//3
        b=n%3
        if b==0:
            tmp=3**a
        elif b==1:
            tmp=3**(a-1)*4
        elif b==2:
            if a>=2:
                tmp=max(3**(a-2)*16,3**a*2)
            else:
                tmp=max(3**(a-1)*5,3**a*2)
        return tmp