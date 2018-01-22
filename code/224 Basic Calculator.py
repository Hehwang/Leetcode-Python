class Solution:
    # 定义一个函数计算括号里的式子
    def helper(self,s):
        length=len(s)
        # 检查时候含有'--','+-'
        s=''.join(s)
        s=s.replace('--','+')
        s=s.replace('+-','-')
        s=[x for x in s if x!='#']
        s=['+']+s[1:-1]+['+']        
        tmp=0
        lastsign=0
        for i in range(1,len(s)):
            if i==1 and s[i]=='-':
                lastsign=1
                continue
            if s[i]=='+' or s[i]=='-':
                tmp+=int(''.join(s[lastsign:i]))
                lastsign=i
        return (list(str(tmp)),(length-len(list(str(tmp)))))        
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s='('+s+')'
        s=[x for x in s if x!=' ']
        stack=[]
        i=0
        while i<len(s):
            if s[i]=='(':
                stack.append(i)
                i+=1
            elif s[i]==')':
                last=stack.pop()
                tmp=self.helper(s[last:i+1])
                s[last:i+1]=tmp[0]
                i-=tmp[1]
            else:
                i+=1
        return int(''.join(s))