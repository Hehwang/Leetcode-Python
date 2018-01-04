class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        dp=[False]*2+[True]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if dp[i]:
                dp[i*i:n:i]=[False]*len(dp[i*i:n:i])
        return sum(dp)