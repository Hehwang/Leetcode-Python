class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letter=[chr(x) for x in range(65,91)]
        if n<=26 and n>0:
            return letter[n-1]
        elif n%26==0:
            return self.convertToTitle(n//26-1)+'Z'
        else:
            return self.convertToTitle(n//26)+letter[n%26-1]