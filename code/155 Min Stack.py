class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a=[]   
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin=self.getMin()
        if len(self.a)==0 or x<curMin:
            curMin=x
        self.a.append((x,curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.a.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.a)==0:
            return None
        return self.a[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.a)==0:
            return None
        return self.a[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()