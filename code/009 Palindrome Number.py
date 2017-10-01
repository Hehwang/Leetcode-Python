class Solution(object):
    def IntegerLength(self,x):
        i=1
        while x//(10**i)>=1:
            i+=1
        return i

    def IthNum(self,x,i):
        length=self.IntegerLength(x)
        if i<=0 or i>length:
            return False
        return x//(10**(i-1))%10
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        i=1
        length=self.IntegerLength(x)
        while i<=length/2:
            if self.IthNum(x,i)==self.IthNum(x,length-i+1):
                i+=1
            else:
                return False
        return True