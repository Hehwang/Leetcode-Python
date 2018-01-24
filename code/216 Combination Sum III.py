class Solution:
    def __init__(self):
        self.res=[]
    def helper(self,path,last,k,n):
        if len(path)==k:
            if sum(path)==n:
                self.res.append(path)
        else:
            for i in range(last,10):
                self.helper(path+[i],i+1,k,n)       
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.helper([],1,k,n)
        return self.res