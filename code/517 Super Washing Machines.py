class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n=len(machines)
        if n<2:
            return 0
        total=sum(machines)
        if total%n!=0:
            return -1
        avg=total//n
        machines=list(map(lambda x:x-avg,machines))
        res=None
        leftCnt=0
        rightCnt=sum(machines[1:])
        for i in range(1,n):
            leftCnt+=machines[i-1]
            rightCnt-=machines[i]
            if leftCnt>=0 and rightCnt>=0:
                tmp=min(leftCnt,rightCnt)
            elif leftCnt<0 and rightCnt<0:
                tmp=-(leftCnt+rightCnt)
            else:
                tmp=max(abs(leftCnt),abs(rightCnt))
            if tmp>res:
                res=tmp        
        return res