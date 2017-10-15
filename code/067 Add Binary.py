class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=list(a)
        b=list(b)
        a.reverse()
        b.reverse()
        maxlength=max(len(a),len(b))
        a=a+[0]*(maxlength-len(a)+1)
        b=b+[0]*(maxlength-len(b)+1)
        res=[0]*(maxlength+1)
        carry=0
        for i in range(len(res)):
            if a[i]==b[i]=='1':
                res[i]=0+carry
                carry=1
            else:
                res[i]=int(a[i])+int(b[i])+carry
                carry=0
                if res[i]==2:
                    res[i]=0
                    carry=1
        res.reverse()
        if res[0]==0:
            res=res[1:]
        return ''.join(list(map(str,res)))