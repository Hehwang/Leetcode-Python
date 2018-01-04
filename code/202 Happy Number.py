class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pastset=set([n])
        while True:
            tmplist=list(str(n))
            tmpsum=sum(list(map(lambda x:int(x)**2,tmplist)))
            if tmpsum==1:
                return True
            if tmpsum in pastset:
                break
            pastset.add(tmpsum)
            n=tmpsum
        return False