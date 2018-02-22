class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J=set(list(J))
        res=0
        for i in S:
            if i in J:
                res+=1
        return res