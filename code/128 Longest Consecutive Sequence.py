class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set(nums)
        res=0
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
                start,end=num-1,num+1
                while start in nums_set:
                    nums_set.remove(start)
                    start-=1
                while end in nums_set:
                    nums_set.remove(end)
                    end+=1
                res=max(res,end-start-1)
        return res