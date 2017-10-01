class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s='#'+'#'.join(s)+'#'
        RL=[0]*len(s)
        MaxRight=0
        pos=0
        MaxLen=0
        for i in range(len(s)):
            if i<MaxRight:
                RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i]=1
            while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
                RL[i]+=1
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
            if RL[i]>MaxLen:
                MaxLen=RL[i]
                res=s[i-RL[i]+1:i+RL[i]]
        return ''.join([x for x in res if x!='#'])