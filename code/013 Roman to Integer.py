class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        res=0
        for i in range(len(s)-1):
            if romanDict[s[i]]<romanDict[s[i+1]]:
                res-=romanDict[s[i]]    
            else:
                res+=romanDict[s[i]]
        return res+romanDict[s[-1]]