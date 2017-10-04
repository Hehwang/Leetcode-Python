class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<2:
            return False
        if k==0:
            for i in range(1,len(nums)):
                if nums[i]==0 and nums[i-1]==0:
                    return True
            else:
                return False

        Arraysum=[]
        tmpsum=0
        for i in range(len(nums)):
            tmpsum+=nums[i]
            Arraysum.append(tmpsum%k)
        tmpDict={}
        for i in range(len(Arraysum)):
            if (Arraysum[i] in tmpDict and i -tmpDict[Arraysum[i]]>=1) or (Arraysum[i]==0 and i>=1):
                return True
            else:
                tmpDict[Arraysum[i]]=i
        return False