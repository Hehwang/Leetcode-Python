class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                tmp=min([x for x in nums[i:] if x>nums[i-1]])
                tmpindex=nums.index(tmp,i-1)
                nums[i:]=sorted(nums[i-1:tmpindex]+nums[tmpindex+1:])
                nums[i-1]=tmp
                flag=1
                break
        if flag==0:
            nums.reverse()