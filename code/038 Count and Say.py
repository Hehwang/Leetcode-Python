class Solution(object):
    def helper(self,s):
        if len(s)==1:
            return [1,1]
        lastnum=s[0]
        tmpcount=1
        res=[]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                tmpcount+=1
            elif s[i]!=s[i-1]:
                res.extend([tmpcount,lastnum])
                lastnum=s[i]
                tmpcount=1
            if i==len(s)-1:
                res.extend([tmpcount,lastnum])
        return res      
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i=1
        s=[1]
        while i<n:
            s=self.helper(s)
            i+=1
        return ''.join(list(map(str,s)))