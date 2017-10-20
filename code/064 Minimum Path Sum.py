class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==j==0:
                    dp[i][j]=grid[0][0]
                elif i==0:
                    dp[i][j]=grid[i][j]+dp[i][j-1]
                elif j==0:
                    dp[i][j]=grid[i][j]+dp[i-1][j]                
                else:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]