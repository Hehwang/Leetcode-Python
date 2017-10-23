class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]==val:
                    flag=0
                    for j in range(len(nums)-1,i,-1):
                        if nums[j]!=val:
                            nums[i],nums[j]=nums[j],nums[i]
                            flag=1
                            break
                    if flag==0:
                        break
            return nums.index(val)