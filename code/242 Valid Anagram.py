class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=collections.Counter(s)
        t=collections.Counter(t)
        for i in list(s.keys())+list(t.keys()):
            if s[i]!=t[i]:
                return False
        return True