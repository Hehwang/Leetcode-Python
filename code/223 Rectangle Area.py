class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        # 分别计算两个面积
        area1=(C-A)*(D-B)
        area2=(H-F)*(G-E)
        
        # 先判断不相交的情况
        if D<=F or H<=B or C<=E or G<=A:
            return area1+area2
        # 相交的情况
        ylist=sorted([D,H,B,F])
        xlist=sorted([A,C,G,E])
        y=ylist[2]-ylist[1]
        x=xlist[2]-xlist[1]
        return area1+area2-y*x