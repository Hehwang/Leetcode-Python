class Solution(object):
    def helper(self,x,n):
        try:
            if n==1:
                return x
            if n%2==1:
                return self.helper(x,(n-1)/2)**2*x
            else:
                return self.helper(x,n/2)**2
        except:
            return 'error'
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return self.helper(1/x,abs(n))
        else:
            return self.helper(x,n)