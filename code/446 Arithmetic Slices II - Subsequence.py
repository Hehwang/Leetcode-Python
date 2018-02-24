class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp=[{} for _ in range(len(A))]
        res=0
        for i in range(len(A)):
            for j in range(i):
                delta=A[i]-A[j]
                if delta in dp[i]:
                    dp[i][delta]+=1
                else:
                    dp[i][delta]=1
                if delta in dp[j]:
                    dp[i][delta]+=dp[j][delta]
                    res+=dp[j][delta]
        return res