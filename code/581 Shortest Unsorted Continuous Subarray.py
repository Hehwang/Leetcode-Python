class Solution(object):
    def helper(self,nums):
        stack1=[nums[0]]
        flag=0
        for i in range(1,len(nums)):
            if nums[i]>=stack1[-1]:
                if flag==0:
                    stack1.append(nums[i])
                    continue
                else:
                    continue
            else:
                flag=1
                while len(stack1)>0 and nums[i]<stack1[-1]:
                    tmp=stack1.pop()                
            if len(stack1)==0:
                break
        return len(stack1)        
    
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res1=self.helper(nums)
        nums.reverse()
        res2=self.helper(list(map(lambda x :-x,nums)))
        return max(len(nums)-(res1+res2),0)