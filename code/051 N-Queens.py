class Solution(object):
    def __init__(self):
        self.res=[]
    def convert2D(self,A):
        res=[None]*len(A)
        for i in range(len(A)):
            tmp=A[i]
            res[i]='.'*tmp+'Q'+'.'*(len(A)-tmp-1)
        return res
    def helper(self,A,cur):
        if cur==len(A):
            self.res.append(self.convert2D(A))
        else:
            for col in range(len(A)):
                A[cur]=col
                flag=True
                for row in range(cur):
                    if abs(row-cur)==abs(A[cur]-A[row]) or A[row]==A[cur]:
                        flag=False
                        break
                if flag:
                    self.helper(A,cur+1)   
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.helper([None]*n,0)
        return self.res