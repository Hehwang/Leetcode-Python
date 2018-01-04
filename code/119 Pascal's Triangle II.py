class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=None
        init=[0,1]
        for i in range(rowIndex+1):
            tmp=[None]*(i+1)
            for i in range(len(init)-1):
                tmp[i]=init[i]+init[i+1]
            res=tmp
            init=[0]+tmp+[0]
        return res        