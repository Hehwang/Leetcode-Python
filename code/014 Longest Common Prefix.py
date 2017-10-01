class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        i=0
        flag=0
        while True:
            for string in strs:
                if len(string)<=i or string[i]!=strs[0][i]:
                    flag=1
                    break
            if flag==1:
                break
            else:
                i+=1
        return strs[0][:i]