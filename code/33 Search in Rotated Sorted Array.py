class Solution:
    def helper(self,nums):
        a,b=0,len(nums)-1
        if nums[a]<=nums[b]:
            return True
        while a+1<b:
            if nums[int((a+b)/2)]>=nums[a]:
                a=int((a+b)/2)
            elif nums[int((a+b)/2)]<nums[a]:
                b=int((a+b)/2)
        return a   
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        pivot=self.helper(nums)
        if pivot is not True:
            nums=nums[pivot+1:]+nums[:pivot+1]
            ###这时候旋转的两段长度是 pivot+1 和 len(nums)-pivot-1 
        if target<nums[0] or target>nums[-1]:
            return -1
        a,b=0,len(nums)-1
        while a<b-1:
            if nums[int((a+b)/2)]<=target:
                a=int((a+b)/2)
            else:
                b=int((a+b)/2)
        if nums[b]==target:
            a=b
        #print(a,b)
        #print(nums)
        if nums[a]==target:
            if pivot is True:
                return a
            else:
                if a<len(nums)-pivot-1:
                    return a+(pivot+1)
                else:
                    return a-(len(nums)-pivot-1)
        return -1