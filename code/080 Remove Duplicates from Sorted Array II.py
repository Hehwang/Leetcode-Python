class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return len(nums)    
        for i in range(len(nums)-1,1,-1):
            if nums[i]==nums[i-1]==nums[i-2]:
                nums[i]=None
        i,j=0,0
        #print(nums)
        while j<len(nums):
            #print(i,j,nums)
            if nums[i]==None:
                while j<len(nums) and nums[j]==None:
                    j+=1
                if j<len(nums):
                    nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        return len([x for x in nums if x!=None])