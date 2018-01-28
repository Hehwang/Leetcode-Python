class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n=len(points)
        distance=[[None]*n for _ in range(n)]
        for i in range(len(points)):
            distance[i][i]=0
            for j in range(i+1,len(points)):
                   distance[i][j]=distance[j][i]=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
        res=0
        for i in range(len(distance)):
            tmp=collections.Counter(distance[i])
            for j in tmp:
                if tmp[j]>=2:
                    res+=(tmp[j]-1)*tmp[j]
        return res