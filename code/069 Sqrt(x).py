class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=0
        high=x
        mid=(low+high)/2.0
        while int(mid)**2>x or (int(mid)+1)**2<=x:
            if mid**2-x<=0:
                low=mid
            else:
                high=mid
            mid=(low+high)/2.0
        return int(mid)
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ### newton iteration
        a=x**2
        b=x
        while int(b)**2>x or (int(b)+1)**2<=x:
            b=(x-a)/(2*b)+b
            a=b**2
        return b
'''