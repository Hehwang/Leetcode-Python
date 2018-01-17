class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        G(n) 表示一个list(range(1,n)) 二叉树组合的数量
        F(i,n) 表示在这里面以i为root的二叉树组合数量
        显然：
        G(n)=F(1,n)+F(2,n)+...+F(n,n)
        F(i,n)=G(i-1)*G(n-i)
        '''
        res=[0]*(n+1)
        res[:2]=[1,1]        
        for i in range(2,n+1):
            for j in range(i):
                res[i]+=res[j]*res[i-1-j]
        return res[-1]