class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n=numRows
        if n==1:
            return s
        a=len(s)//(2*n-2)
        b=len(s)%(2*n-2)
        if b<=n:
            flag=0
            rowmark=b
        else:
            flag=1
            rowmark=n-(b-n)
        res=[]
        for i in range(1,n+1):
            if i==1:
                tmp=1
                for j in range(a):
                    res.append(s[tmp-1])
                    tmp+=2*n-2
                if b!=0:
                    res.append(s[tmp-1])
            elif i==n:
                tmp=n
                for j in range(a):
                    res.append(s[tmp-1])
                    tmp+=2*n-2
                if rowmark==n or flag==1:
                    res.append(s[tmp-1])              
            else:
                tmp=i
                for j in range(a):
                    res.append(s[tmp-1])
                    tmp2=tmp+2*(n-i)
                    res.append(s[tmp2-1])
                    tmp+=2*n-2
                if i<=rowmark:
                    res.append(s[tmp-1])
                elif i>rowmark  and flag==1:
                    res.append(s[tmp-1])
                    res.append(s[tmp+2*(n-i)])   
        return ''.join(res)           
