class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Arraysum=[]
        tmpsum=0
        for i in range(len(nums)):
            if nums[i]==0:
                tmpsum+=-1
            else:
                tmpsum+=1
            Arraysum.append(tmpsum)
        
        tmpDict={}
        tmplen=0
        res=0
        for i in range(len(Arraysum)):
            if Arraysum[i] in tmpDict:
                tmplen=i-tmpDict[Arraysum[i]]
            elif Arraysum[i]==0:
                tmplen=i+1
            else:
                tmpDict[Arraysum[i]]=i
            res=max(res,tmplen)
        return res