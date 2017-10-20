class Solution(object):
    def helper(self,n):
        res=1
        while n>1:
            res*=n
            n-=1
        return res
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.helper(m+n-2)/self.helper(n-1)/self.helper(m-1)