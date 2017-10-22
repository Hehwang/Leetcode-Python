class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        dp=[None]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        for i in range(1,len(s)):
            if s[i-1]=='0':
                if s[i]=='0':
                    return 0
                else:
                    dp[i+1]=dp[i]
            elif s[i-1]<'2':
                if s[i]=='0':
                    dp[i+1]=dp[i-1]
                else:
                    dp[i+1]=dp[i]+dp[i-1]
            elif s[i-1]=='2':
                if s[i]<'7' and s[i]>'0':
                    dp[i+1]=dp[i]+dp[i-1]
                elif s[i]=='0':
                    dp[i+1]=dp[i-1]
                else:
                    dp[i+1]=dp[i]
            else:
                if s[i]=='0':
                    return 0
                else:
                    dp[i+1]=dp[i]         
        return dp[-1]