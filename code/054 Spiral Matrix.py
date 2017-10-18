class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        rows=len(matrix)
        cols=len(matrix[0])
        mask=[[True]*cols for _ in range(rows)]
        direction=[[0,1],[1,0],[0,-1],[-1,0]]
        i,j=0,0
        D=0
        res=[]
        count=0
        while count<rows*cols:
            res.append(matrix[i][j])
            mask[i][j]=False
            if i+direction[D][0]<rows and j+direction[D][1]<cols and mask[i+direction[D][0]][j+direction[D][1]]:
                i+=direction[D][0]
                j+=direction[D][1]
            else:
                D+=1
                if D==4:
                    D=0
                i+=direction[D][0]
                j+=direction[D][1]
            count+=1
        return res