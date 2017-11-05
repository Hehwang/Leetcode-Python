class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path=[x for x in path.split('/') if (x!='' and x!='.')]
        stack=[]
        for i in path:
            if i=='..': 
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)