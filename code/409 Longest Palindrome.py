class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        s=dict(collections.Counter(list(s)))
        res=0
        for i in s:
            if s[i]%2==0:
                tmp=s[i]
            else:
                tmp=s[i]-1
            res+=tmp
        return res if res==n else res+1