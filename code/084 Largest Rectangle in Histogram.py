class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack=[]
        max_area=0
        i=0
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