class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        ans=0
        for i in range(2,len(nums)):
            a,b=0,i-1
            while a<b:
                if nums[a]+nums[b]>nums[i]:
                    ans+=b-a
                    b-=1
                else:
                    a+=1
        return ans
            