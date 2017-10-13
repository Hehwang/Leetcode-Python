class Solution(object):
    def twoSum(self,nums,target):
        left=0
        right=len(nums)-1
        res=[]
        while left<right:
            if nums[left]+nums[right]==target:
                res.append([nums[left],nums[right]])
                while left+1<right and nums[left+1]==nums[left]:
                    left+=1
                while right-1>left and nums[right-1]==nums[right]:
                    right-=1
                left+=1
                right-=1
            elif nums[left]+nums[right]<target:
                left+=1
            elif nums[left]+nums[right]>target:
                right-=1
        return res
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                tmp=self.twoSum(nums[i+1:],-nums[i])
                if len(tmp)>0:
                    for j in tmp:
                        res.append([nums[i]]+j)
        return res