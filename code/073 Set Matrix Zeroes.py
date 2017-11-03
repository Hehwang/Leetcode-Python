class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row=[False]*len(matrix)
        col=[False]*len(matrix[0])
        for i in range(len(row)):
            for j in range(len(col)):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i] or col[j]:
                    matrix[i][j]=0