class Solution(object):
    def __init__(self):
        self.res=[]
    def helper(self,nums,tmp,target,index):
        if sum(tmp)==target:
            self.res.append(tmp)
        elif sum(tmp)<target:
            for i in range(index,len(nums)):
                self.helper(nums,tmp+[nums[i]],target,i)        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.helper(candidates,[],target,0)
        return self.res