class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        tmpDict={'(':')','{':'}','[':']'}
        stack=[]
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
                continue
            if stack[-1] in tmpDict and s[i]==tmpDict[stack[-1]]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)==0