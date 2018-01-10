class Solution(object):
    def __init__(self):
        self.mask=None
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
                    if i+dd[0]>=0 and i+dd[0]<n and j+dd[1]>=0 and j+dd[1]<m and self.mask[i+dd[0]][j+dd[1]] and board[i+dd[0]][j+dd[1]]=='O':
                        queue2.append([i+dd[0],j+dd[1]])
                        self.mask[i+dd[0]][j+dd[1]]=False
            queue=queue2        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """     
        n=len(board)
        if n>0:
            m=len(board[0])
            self.mask=[[True]*m for _ in range(n)]
            for j in range(m):
                if board[0][j]=='O':
                    self.helper([0,j],board,m,n)
                if board[n-1][j]=='O':
                    self.helper([n-1,j],board,m,n)
            for i in range(n):
                if board[i][0]=='O':
                    self.helper([i,0],board,m,n)
                if board[i][m-1]=='O':
                    self.helper([i,m-1],board,m,n)
            for i in range(n):
                for j in range(m):
                    if self.mask[i][j]:
                        board[i][j]='X'