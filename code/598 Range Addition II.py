class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for operation in ops:
            m=min(m,operation[0]) 
            n=min(n,operation[1])
        return m*n