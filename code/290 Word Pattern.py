class Solution(object):
    ##  transform string 
    def helper1(self,s):
        tmpdict={}
        res=''
        for i in range(len(s)):
            if not s[i] in tmpdict:
                tmpdict[s[i]]=str(i)
                res+=str(i)
            else:
                res+=tmpdict[s[i]]
        return res
    ## transform list
    def helper2(self,s):
        tmpdict={}
        res=''
        s=[x for x in s.split()]
        for i in range(len(s)):
            if not s[i] in tmpdict:
                tmpdict[s[i]]=str(i)
                res+=str(i)
            else:
                res+=tmpdict[s[i]]
        return res
        
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.helper1(pattern)==self.helper2(str)