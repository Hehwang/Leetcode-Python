class Solution:
    def __init__(self):
        self.res=[]
    def helper(self,path,string):
        if len(path)==4: 
            if len(string)==0:
                self.res.append(path)
        else:
            for i in range(min(3,len(string))):
                if string[0]=='0':
                    if i==0:
                        self.helper(path+[string[:i+1]],string[i+1:])
                elif int(string[:i+1])<=255:
                    self.helper(path+[string[:i+1]],string[i+1:])  
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        self.helper([],s)
        for i in self.res:
            res.append('.'.join(i))
        return res