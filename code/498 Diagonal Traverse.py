class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row=len(matrix)
        if row==0:
            return []
        col=len(matrix[0])
        res=[]
        flag=-1
        count_col,count_row=0,0
        for i in range(0,row+col-1):
            tmp=[]
            if i<col:
                count_row+=1
                for j in range(0,min(i+1,row)):
                    if i-j<col and j<row:                       
                        tmp.append(matrix[j][i-j])
            else:
                count_col+=1
                for j in range(count_col,min(row,i+1)):
                    if i-j<col and j<row:  
                        tmp.append(matrix[j][i-j])                      
            if flag==-1:
                tmp.reverse()
            flag*=-1
            res.extend(tmp)
        return res