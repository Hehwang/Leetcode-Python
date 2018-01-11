class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1)<len(num2):
            num1,num2=num2,num1
        num1=['0']+list(num1)
        num1.reverse()
        num2=['0']+list(num2)
        num2.reverse()
        num2.extend([0]*(len(num1)-len(num2)))
        res=[0]*len(num1)
        for i in range(len(num1)-1):
            tmp=int(num1[i])+int(num2[i])
            res[i]+=tmp%10
            if res[i]>9:
                res[i]=res[i]%10
                res[i+1]+=1   
            res[i+1]+=tmp//10
        res.reverse()
        if res[0]==0:
            res=res[1:]
        return ''.join(list(map(str,res)))