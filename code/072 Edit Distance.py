class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1)==0 or len(word2)==0:
            return max(len(word1),len(word2))    
        dp=[[None]*len(word2) for _ in range(len(word1))]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i==j==0:
                    if word1[i]==word2[j]:
                        dp[i][j]=0
                    else:
                        dp[i][j]=1
                elif i==0:
                    if word1[i]==word2[j]:
                        dp[i][j]=max(dp[i][j-1],j)
                    else:
                        dp[i][j]=dp[i][j-1]+1
                elif j==0:
                    if word1[i]==word2[j]:
                        dp[i][j]=max(dp[i-1][j],i)
                    else:
                        dp[i][j]=dp[i-1][j]+1
                else:
                    if word1[i]==word2[j]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1       
        return dp[-1][-1]