# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=1,n
        while True:
            mid=int((a+b)/2)
            if guess(mid)==0:
                return mid
            elif guess(mid)==-1:
                b=mid-1
            else:
                a=mid+1