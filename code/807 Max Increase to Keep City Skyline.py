class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max,col_max=[],[]
        for i in range(len(grid)):
            row_max.append(max(grid[i]))
        for i in range(len(grid[0])):
            col_max.append(max([x[i] for x in grid]))
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res+=min(row_max[i],col_max[j])-grid[i][j]
        return res
            