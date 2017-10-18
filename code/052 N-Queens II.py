class Solution(object):
    def __init__(self):
        self.res=0
    def helper(self,A,cur):
        if cur==len(A):
            self.res+=1
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
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.helper([None]*n,0)
        return self.res