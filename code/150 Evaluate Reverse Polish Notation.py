class Solution:  
    def helper(self,a,b,operator):
        a,b=int(a),int(b)
        if operator=='+':
            return a+b
        elif operator=='-':
            return a-b
        elif operator=='*':
            return a*b
        elif operator=='/':
            return a/b
        else:
            print('BULLSHIT')
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators=set(['+','-','*','/'])
        stack=[]
        for num in tokens:
            if num in operators:
                b=stack.pop()
                a=stack.pop()
                stack.append(self.helper(a,b,num))
            else:
                stack.append(num)
        return int(stack[0])