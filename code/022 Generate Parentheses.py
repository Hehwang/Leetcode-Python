class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,path,left,right,n):
        if right==left==n:
            self.res.append(''.join(path))
        elif right<=n and left<=n and left>=right:
            for i in ['(',')']:
                if i=='(':
                    self.helper(path+['('],left+1,right,n)
                else:
                    self.helper(path+[')'],left,right+1,n)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.helper([],0,0,n)
        return self.res