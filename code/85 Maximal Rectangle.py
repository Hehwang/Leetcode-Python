class Solution(object):
    def histogram(self,heights):
        if len(heights)<2:
            return heights[0] if len(heights)==1 else 0
        heights.append(0)
        max_area=0
        i=0
        stack=[]
        while i<len(heights):
            if len(stack)==0 or heights[stack[-1]]<heights[i]:
                stack.append(i)
                i+=1
            else:
                tmp=stack.pop()
                if len(stack)==0:
                    tmp_area=heights[tmp]*i
                else:
                    tmp_area=heights[tmp]*(i-stack[-1]-1)
                max_area=max(max_area,tmp_area)
        return max_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        matrix=[list(map(lambda y:int(y),list(x))) for x in matrix] 
        
    
        matrix_s=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if i==0:
                    matrix_s[i][j]=matrix[i][j]
                else:
                    if matrix[i][j]==0:
                        matrix_s[i][j]=0
                    elif matrix[i][j]==1:
                        matrix_s[i][j]=matrix_s[i-1][j]+1
        res=0
        for i in range(len(matrix_s)):
            res=max(res,self.histogram(list(matrix_s[i])))
        return res
        