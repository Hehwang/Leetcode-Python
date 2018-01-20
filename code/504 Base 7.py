class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        flag=True if num>0 else False
        num=abs(num)
        res=[]
        while num:
            res.append(str(num%7))
            num=num//7
        res.reverse()
        return '-'+''.join(res) if not flag else ''.join(res)
        