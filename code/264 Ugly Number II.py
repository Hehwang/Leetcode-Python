class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        waiting=set([])
        res=1
        for _ in range(n-1):
            for i in [2,3,5]:
                waiting.add(res*i)
            res=min(waiting)
            waiting.remove(res)
        return res
        '''
        res=[1]
        index1,index2,index3=0,0,0
        for _ in range(n-1):
            num1,num2,num3=res[index1]*2,res[index2]*3,res[index3]*5
            num=min(num1,num2,num3)
            res.append(num)
            if num==num1:
                index1+=1
            if num==num2:
                index2+=1
            if num==num3:
                index3+=1
        return res[-1]