class Solution(object):
    def twoSum(self,nums,target):
        left=0
        right=len(nums)-1
        tmpmin=abs(target-nums[left]-nums[right])
        res=nums[left]+nums[right]
        while left<right:
            if abs(nums[left]+nums[right]-target)<tmpmin:
                tmpmin=abs(nums[left]+nums[right]-target)
                res=nums[left]+nums[right]
            if nums[left]+nums[right]<=target:
                left+=1
            elif nums[left]+nums[right]>target:
                right-=1
        return res
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        tmpmin=abs(target-sum(nums[:3]))
        res=sum(nums[:3])
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                tmp=self.twoSum(nums[i+1:],target-nums[i])
                if abs(tmp+nums[i]-target)<tmpmin:
                    tmpmin=abs(tmp+nums[i]-target)
                    res=tmp+nums[i]
        return res      