class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A,B=0,0
        secret_dict=dict(collections.Counter(secret))
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                A+=1
                secret_dict[guess[i]]-=1
        for i in range(len(secret)):
            if secret[i]!=guess[i] and guess[i] in secret_dict and secret_dict[guess[i]]>0:
                B+=1
                secret_dict[guess[i]]-=1
        return '%dA%dB'%(A,B)