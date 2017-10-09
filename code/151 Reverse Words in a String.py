class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        ##'str' object does not support item assignment in Python
        ## so we assume that given a str list 
        ## and can solve it with O(1) space and O(n) time

        s=list(s)
        flag=0
        for i in range(len(s)):
            if flag==0 and s[i]==' ':
                s[i]=''
                continue
            flag=1
            if s[i]==' ':
                if i==len(s)-1:
                    s[i]=''
                elif s[i+1]==' ':
                    s[i]=''
        strlen=len(s)
        for i in range(int(len(s)/2)):
            s[i],s[strlen-1-i]=s[strlen-1-i],s[i]
        s=[' ']+s+[' ']
        lastindex=0
        for i in range(1,len(s)):
            if s[i]==' ':
                for j in range(lastindex+1,lastindex+int((i-lastindex+1)/2)):
                    s[j],s[i-(j-lastindex)]=s[i-(j-lastindex)],s[j]
                lastindex=i
        s=s[1:-1]
        return ''.join(s)