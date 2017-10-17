class Solution(object):
    def helper(self,s,flag):
        start=-1
        locallen=0
        globallen=0
        leftcount=0
        rightcount=0
        for i in range(len(s)):
            if s[i]==flag:
                leftcount+=1
            else:
                rightcount+=1
            if rightcount>leftcount:
                start=i
                rightcount=0
                leftcount=0
            elif rightcount==leftcount:
                locallen=i-start
                globallen=max(globallen,locallen)
        return globallen
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=self.helper(s,'(')
        tmp=list(s)
        tmp.reverse()
        b=self.helper(''.join(tmp),')')
        return max(a,b)       