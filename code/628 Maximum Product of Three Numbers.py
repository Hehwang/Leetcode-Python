class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        虽然AC了，但是有一个BUG：所给nums内的元素如果都是负数，这个代码是错误的
        
        测试用例待补充
        '''
        res=nums[0]*nums[1]*nums[2]
        p1,p2,p3=None,None,None
        n1,n2=None,None
        for num  in nums:
            if num>=0:
                if (not p1) or num>p1:
                    p3=p2
                    p2=p1
                    p1=num
                elif (not p2) or num>p2:
                    p3=p2
                    p2=num
                elif (not p3) or num>p3:
                    p3=num
            else:
                if (not n1) or num<n1:
                    n2=n1
                    n1=num
                elif (not n2) or num<n2:
                    n2=num    
        if n2 and p1:
            res=max(res,n1*n2*p1)
        if p3:
            res=max(res,p1*p2*p3)
        return res