class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=list(num1)
        num2=list(num2)
        num1.reverse()
        num2.reverse()
        len1=len(num1)
        len2=len(num2)
        ###creat a new list records nums in every digit
        digits=[0]*(len1+len2+2)
        for i in range(len(digits)):
            tmp=0
            for j in range(i+1):
                if j<len1 and i-j<len2:
                    tmp+=int(num1[j])*int(num2[i-j])
            digits[i]=tmp
        for i in range(len(digits)):
            if digits[i]>99:
                digits[i+2]+=digits[i]//100
                digits[i+1]+=digits[i]%100//10
                digits[i]=digits[i]%10
            elif digits[i]>9:
                digits[i+1]+=digits[i]//10
                digits[i]=digits[i]%10 
        digits.reverse()
        i=0
        while digits[0]==0:
            if len(digits)==1:
                return '0'
            digits=digits[1:]
        return ''.join(list(map(str,digits)))