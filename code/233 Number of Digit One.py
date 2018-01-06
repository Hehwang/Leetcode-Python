class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        digit=1
        res=0
        while True:
            a=n//digit
            if a==0:
                break
            b=n%digit
            res+=(a+8)/10*digit+(a%10==1)*(b+1)
            digit*=10
        return res