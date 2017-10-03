class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        localsum=0
        start=0
        minlen=len(nums)+1
        res=len(nums)+1
        for i in range(len(nums)):
            localsum+=nums[i]
            while localsum>=s:
               minlen=min(minlen,i-start+1)
               localsum-=nums[start]
               if localsum<s:
                   localsum+=nums[start]
                   break
               start+=1
            res=min(res,minlen)
        return res if res<=len(nums) else 0