class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in range(int(area**0.5),0,-1):
            if area%i==0:
                return [int(area/i),i]