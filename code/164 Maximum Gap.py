class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        桶排序+抽屉原理
        '''
        
        if len(nums)<2:
            return 0
        max_num=max(nums)
        min_num=min(nums)
        n=len(nums)
        if n==2:
            return max_num-min_num
        bucket=(max_num-min_num)/(n-1)
        if bucket==0:
            return 0
        max_list=[None]*(n-1)
        min_list=[None]*(n-1)
        for i in range(len(nums)):
            index=int((nums[i]-min_num)/bucket)
            if nums[i]==max_num:
                index = -1
            if not max_list[index]:
                max_list[index]=nums[i]
            else:
                max_list[index]=max(max_list[index],nums[i])
            if not min_list[index]:
                min_list[index]=nums[i]
            else:
                min_list[index]=min(min_list[index],nums[i])
        gap=0
        max_list=[max_list[0]]+[x for x in max_list[1:-1] if x]+[max_list[-1]]
        min_list=[min_list[0]]+[x for x in min_list[1:-1] if x]+[min_list[-1]]
        for i in range(1,len(max_list)):
            if min_list[i] and max_list[i-1]:
                gap=max(gap,min_list[i]-max_list[i-1])
        return gap