class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
		### DFS will TLE 	
        if len(s3)!=len(s1)+len(s2):
            return False
        dp=[[0]*(len(s1)+1) for _ in range(len(s2)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==j==0:
                    dp[i][j]=True  
                    continue
                if (j>0 and dp[i][j-1] and s3[i+j-1]==s1[j-1]) or (i>0 and dp[i-1][j] and s3[i+j-1]==s2[i-1]):
                    dp[i][j]=True
                else:
                    dp[i][j]=False
        return dp[-1][-1]