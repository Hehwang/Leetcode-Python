class Solution:
    def helper(self,target,string):
        i,j=0,0
        while i<len(target) and j<len(string):
            if target[i]==string[j]:
                i+=1
                j+=1
            else:
                i+=1
        return j==len(string)
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res=''
        for string in d:
            if self.helper(s,string): 
                if len(string)>len(res):
                    res=string
                elif len(string)==len(res) and string<res:
                    res=string
        return res   