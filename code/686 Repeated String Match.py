class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B not in A*(int(len(B)/len(A))+2):
            return -1
        elif B==A*(int(len(B)/len(A))):
            return int(len(B)/len(A))
        elif B in A*(int(len(B)/len(A))+1):
            return int(len(B)/len(A))+1
        else:
            return int(len(B)/len(A))+2