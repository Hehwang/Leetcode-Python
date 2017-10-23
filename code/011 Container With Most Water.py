class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        globalmax=min(height[i],height[j])*(j-i)
        while True:
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
            if i<j:
                globalmax=max(globalmax,min(height[i],height[j])*(j-i))
            else:
                break
        return globalmax   