class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x+y<z:
            return False
        if not z:
            return True
        while y:
            r=x%y
            x=y
            y=r
        return not bool(z%x)