class Solution(object):
    def helper(self,s):
        tmpdict={}
        res=''
        for i in range(len(s)):
            if not s[i] in tmpdict:
                tmpdict[s[i]]=str(i)
                res+=str(i)
            else:
                res+=tmpdict[s[i]]
        return res    
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.helper(s)==self.helper(t)