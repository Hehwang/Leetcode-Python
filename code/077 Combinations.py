class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,k,path,index,n):
        if index<=n-k:
            if k==0:
                self.res.append(path)
            else:
                for i in list(range(index+1,n+1)):
                    self.helper(k-1,path+[i],i,n)
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.helper(k,[],0,n)
        return self.res