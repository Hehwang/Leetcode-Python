class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        delta=[]
        for i in range(1,len(A)):
            delta.append(A[i]-A[i-1])
        dp=[0]
        for i in range(1,len(delta)):
            if delta[i]==delta[i-1]:
                dp.append(dp[-1]+1)
            else:
                dp.append(0)
        return sum(dp)