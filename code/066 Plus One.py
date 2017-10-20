class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits+=[0]
        digits[0]+=1
        carry=0
        for i in range(len(digits)):
            tmp=digits[i]+carry
            carry=0
            if tmp>9:
                digits[i]=tmp-10
                carry=1
            else:
                digits[i]=tmp
        digits.reverse()
        if digits[0]>0:
            return digits
        else:
            return digits[1:]