class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def hh(nums,i,tmp):
            #global res
            if i==len(nums):
                res.append(tmp)
            else:
                for j in [0,1]:
                    if j==0:
                        hh(nums,i+1,tmp)
                    else:
                        hh(nums,i+1,tmp+[nums[i]])
        hh(nums,0,[])
        return res