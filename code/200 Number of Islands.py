class Solution(object):
    def __init__(self):
        self.mask=None
        self.num_islands=0
    def helper(self,start,board,m,n):
        self.mask[start[0]][start[1]]=False
        queue=[start]
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        while len(queue)>0:
            queue2=[]
            for point in queue:
                i=point[0]
                j=point[1]
                for dd in d:
                    if i+dd[0]>=0 and i+dd[0]<n and j+dd[1]>=0 and j+dd[1]<m and self.mask[i+dd[0]][j+dd[1]] and board[i+dd[0]][j+dd[1]]=='1':
                        queue2.append([i+dd[0],j+dd[1]])
                        self.mask[i+dd[0]][j+dd[1]]=False
            queue=queue2   
        self.num_islands+=1
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n=len(grid)
        if n==0:
            return 0   
        m=len(grid[0])
        self.mask=[[True]*m for _ in range(n)]
        res=0
        for j in range(m):
            for i in range(n):
                if grid[i][j]=='1' and self.mask[i][j]:
                    self.helper([i,j],grid,m,n)
        return self.num_islands