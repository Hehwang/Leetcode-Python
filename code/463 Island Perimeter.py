class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=len(grid)
        c=len(grid[0])
        num=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    if (i>=1 and grid[i-1][j]==0) or i==0:
                        num+=1
                    if (i+1<=r-1 and grid[i+1][j]==0) or i==r-1:
                        num+=1
                    if (j>=1 and grid[i][j-1]==0) or j==0:
                        num+=1
                    if (j+1<=c-1 and grid[i][j+1]==0) or j==c-1:
                        num+=1
        return num