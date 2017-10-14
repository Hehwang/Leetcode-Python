class Solution(object):
    def __init__(self):
        self.res=[]
        self.digitsDict={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
    def helper(self,digits,path,index):
        if index==len(digits):
            self.res.append(''.join(path))
        else:
            for i in self.digitsDict[digits[index]]:
                self.helper(digits,path+[i],index+1)        
    def letterCombinations(self,digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.helper(digits,[],0)
        return self.res if len(digits)!=0 else []