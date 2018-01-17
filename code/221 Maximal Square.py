class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 初始化dp
        
        if len(matrix)==0:
            return 0
        dp=[[None]*len(matrix[0]) for _ in range(len(matrix))]
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 or j==0:
                    dp[i][j]=int(matrix[i][j])
                elif matrix[i][j]=='0':
                    dp[i][j]=0
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                if dp[i][j]>res:
                    res=dp[i][j]
        return res**2