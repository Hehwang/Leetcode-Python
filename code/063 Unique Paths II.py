class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        mask=[[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i==j==0:
                    mask[i][j]=1
                elif i==0:
                    if obstacleGrid[i][j]==0:
                        mask[i][j]=mask[i][j-1]
                    else:
                        mask[i][j]=0
                elif j==0:
                    if obstacleGrid[i][j]==0:
                        mask[i][j]=mask[i-1][j]
                    else:
                        mask[i][j]=0 
                else:
                    if obstacleGrid[i][j]==0:
                        mask[i][j]=mask[i-1][j]+mask[i][j-1]
                    else:
                        mask[i][j]=0 
        return mask[-1][-1]