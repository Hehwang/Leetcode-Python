class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[None]*(len(p)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                dp[i][j]=False
        dp[0][0]=True
        for i in range(len(s)+1):
            for j in range(1,len(p)+1):
                if i>0 and (s[i-1]==p[j-1] or p[j-1]=='.'):
                    dp[i][j]=dp[i-1][j-1]
                if p[j-1]=='*':
                    if i==0 or (s[i-1]!=p[j-2] and p[j-2]!='.'):
                        dp[i][j]=dp[i][j-2]
                    else:
                        dp[i][j]=dp[i-1][j] or dp[i][j-1] or dp[i][j-2]
        return dp[-1][-1]