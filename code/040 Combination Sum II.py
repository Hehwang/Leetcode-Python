class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,nums,tmp,target,index):
        if sum(tmp)==target:
            self.res.append(tmp)
        elif sum(tmp)<target:
            for i in range(index,len(nums)):
                if nums[i]==nums[i-1] and i>index:
                    continue
                self.helper(nums,tmp+[nums[i]],target,i+1)  
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates=sorted(candidates)
        self.helper(candidates,[],target,0)
        return self.res