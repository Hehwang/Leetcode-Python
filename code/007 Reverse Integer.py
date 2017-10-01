class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=0
        MaxInt=2**31
        if x<0:flag=1
        tmp=list(str(abs(x)))
        tmp.reverse()
        res=int(''.join(tmp))   
        if abs(res)>MaxInt:
            return 0
        return -res if flag==1 else res