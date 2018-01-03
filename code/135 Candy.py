class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res=0
        n=len(ratings)
        l,r=[1]*n,[1]*n
        for i in range(1,len(ratings)):            
            if ratings[i]>ratings[i-1]:
                l[i]=l[i-1]+1
            if ratings[n-i-1]>ratings[n-i]:
                r[n-i-1]=r[n-i]+1
        for i in range(n):
            res+=max(l[i],r[i])
        return res