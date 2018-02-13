class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_nums=sorted(nums,reverse=True)
        rank=1
        rank_dict={}
        rank_dict[sorted_nums[0]]=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                rank+=1
                rank_dict[sorted_nums[i]]=rank
        for i in range(len(nums)):
            nums[i]=rank_dict[nums[i]]
            if nums[i]==1:
                nums[i]='Gold Medal'
            elif nums[i]==2:
                nums[i]='Silver Medal'
            elif nums[i]==3:
                nums[i]='Bronze Medal'
            else:
                nums[i]=str(nums[i])
        return nums