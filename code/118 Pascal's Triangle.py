class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[]
        init=[0,1]
        for i in range(numRows):
            tmp=[None]*(i+1)
            for i in range(len(init)-1):
                tmp[i]=init[i]+init[i+1]
            res.append(tmp)
            init=[0]+tmp+[0]
        return res