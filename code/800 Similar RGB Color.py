class Solution:
    def helper1(self,s):
        tmp1={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
        if s in tmp1:
            return tmp1[s]
        else:
            return int(s)
    def helper2(self,s):
        tmp1={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        if s[0]==s[1]: 
            return s
        num=self.helper1(s[0])*16+self.helper1(s[1])
        num1=self.helper1(s[0])*16+self.helper1(s[0])
        if num<num1:
            tmp=self.helper1(s[0])-1
            num2=tmp*16+tmp
            if abs(num-num1)<abs(num-num2):
                return s[0]*2
            else:
                if tmp>=10:
                    return tmp1[tmp]*2
                else:
                    return str(tmp)*2
        else:
            tmp=self.helper1(s[0])+1
            num2=tmp*16+tmp
            if abs(num-num1)<abs(num-num2):
                return s[0]*2
            else:
                if tmp>=10:
                    return tmp1[tmp]*2
                else:
                    return str(tmp)*2            
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        a=self.helper2(color[1:3])
        b=self.helper2(color[3:5])
        c=self.helper2(color[5:7])
        return '#'+a+b+c