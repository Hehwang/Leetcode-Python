class Solution:
    def __init__(self):
        self.res=[]
    def helper1(self,s):
        return s==s[::-1]
    def helper2(self,path,s):
        if len(s)==0:
            self.res.append(path)
        else:
            for i in range(len(s)):
                if self.helper1(s[:i+1]):
                    self.helper2(path+[s[:i+1]],s[i+1:])            
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.helper2([],s)
        return self.res