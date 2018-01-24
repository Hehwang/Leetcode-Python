class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        start,end=0,0
        muti=1
        res=0
        while end<len(nums):
            #print("input",start,end,muti,res)
            muti*=nums[end]
            end+=1
            while muti>=k and start<end:
                muti/=nums[start]
                start+=1          
            res+=end-start
            #print("output",start,end,muti,res)
        return res