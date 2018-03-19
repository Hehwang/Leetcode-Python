# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def gcd(self,x,y): 
        if y==0 :
            return x 
        else:
            return self.gcd(y, x%y)    
    def helper(self,a,b):
        if a.x-b.x==0:
            return (a.x,'max')
        else:
            if a.y-b.y==0:
                k=(0,0)
            else:
                tmp=self.gcd(a.y-b.y,a.x-b.x)
                k=(int((a.y-b.y)/tmp),int((a.x-b.x)/tmp))
            if k[1]<0:
                k=(-k[0],-k[1])
            if a.y*b.x-b.y*a.x==0:
                b=(0,0)
            else:
                tmp=self.gcd(a.y*b.x-b.y*a.x,b.x-a.x)
                b=(int((a.y*b.x-b.y*a.x)/tmp),int((b.x-a.x)/tmp))
                if b[1]<0:
                    b=(-b[0],-b[1])
            return k+b
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        
        num_dict={}
        i=0
        while i<len(points):
            if (points[i].x,points[i].y) in num_dict:
                num_dict[(points[i].x,points[i].y)]+=1
                points=points[:i]+points[i+1:]
            else:
                num_dict[(points[i].x,points[i].y)]=1
                i+=1
        if len(points)==0:
            return 0
        if len(points)==1:
            return num_dict[(points[0].x,points[0].y)]
        pointsdict={}
        countdict={}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                tmp=self.helper(points[i],points[j])
                if tmp in pointsdict:  
                    if (points[i].x,points[i].y) not in pointsdict[tmp]:
                        pointsdict[tmp].add((points[i].x,points[i].y))
                        countdict[tmp]+=num_dict[(points[i].x,points[i].y)]
                    if (points[j].x,points[j].y) not in pointsdict[tmp]:
                        pointsdict[tmp].add((points[j].x,points[j].y))
                        countdict[tmp]+=num_dict[(points[j].x,points[j].y)]                        
                else:
                    pointsdict[tmp]=set([(points[i].x,points[i].y),(points[j].x,points[j].y)])
                    countdict[tmp]=num_dict[(points[i].x,points[i].y)]+num_dict[(points[j].x,points[j].y)]
        #print(num_dict,pointsdict,countdict)
        res=1
        for i in countdict:
            res=max(res,countdict[i])
        return res
                    