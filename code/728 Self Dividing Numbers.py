class Solution(object):    
    def helper(self,num):
        num_s=str(num)
        for i in range(len(num_s)):
            if num_s[i]=="0":
                return False
            elif num%int(num_s[i])!=0:
                return False
        return True
    
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            if self.helper(i):
                res.append(i)
        return res