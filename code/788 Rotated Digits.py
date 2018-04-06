class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        set1=set(['2','5','6','9'])
        set2=set(['3','4','7']) 
        count=0
        for i in range(1,N+1):
            flag1=True
            flag2=False
            tmp=list(set(str(i)))
            for num in tmp:
                if num in set2:
                    flag1=False
                elif num in set1:
                    flag2=True
            if flag1 and flag2:
                count+=1
        return count
                    