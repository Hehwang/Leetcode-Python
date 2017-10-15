class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp=s.split()
        return len(tmp[-1]) if len(tmp)>0 else 0