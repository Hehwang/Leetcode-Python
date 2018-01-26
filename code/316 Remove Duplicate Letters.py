class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ''
        tmpdict=dict(collections.Counter(s))
        stack=[s[0]]
        for i in range(1,len(s)):
            #print(stack,tmpdict)
            if s[i] in stack:
                tmpdict[s[i]]-=1
                continue
            if s[i]>stack[-1]:
                stack.append(s[i])
                continue
            else:
                while len(stack)>0 and s[i]<=stack[-1] and tmpdict[stack[-1]]>1: 
                    tmp=stack.pop()
                    tmpdict[tmp]-=1   
                stack.append(s[i])               
        return ''.join(stack)