class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s)==0:
            return True
        if len(wordDict)==0:
            return False
        
        ##calculate the max length of words

        max_length=0
        for word in wordDict:
            max_length=max(max_length,len(word))
        
        dp=[False for _ in range(len(s)+1)]
        dp[0]=True
        for i in range(1,len(dp)):
            j=1
            while j<=max_length and j<=i:
                if not dp[i-j]:
                    j+=1
                    continue
                if s[i-j:i] in wordDict:
                    dp[i]=True
                    break
                j+=1
        return dp[-1]