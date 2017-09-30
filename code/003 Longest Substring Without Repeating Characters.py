class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        maxlength =0
        lastindex=-1
        length=0
        for i in range(len(s)):
            if not(s[i] in dict):
                dict[s[i]]=i
                length=i-lastindex
            else:
                newlastindex=dict[s[i]]
                if newlastindex>lastindex:
                    lastindex=newlastindex
                length=i-lastindex
                dict[s[i]]=i
            if length>maxlength:
                maxlength=length
        return maxlength        