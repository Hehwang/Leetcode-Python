class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if len(b)==1:
            return a**b[0]
        else:
            return ((((self.superPow(a,b[:-1]))%1337)**10)%1337*(a**b[-1]%1337))%1337