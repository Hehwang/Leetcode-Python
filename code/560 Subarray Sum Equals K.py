class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        Arraysum=[]
        tmpsum=0
        for i in range(len(nums)):
            tmpsum+=nums[i]
            Arraysum.append(tmpsum)
            
        tmpDict={}
        count=0
        flag=1
        for i in range(len(Arraysum)):
            if Arraysum[i]-k in tmpDict:
                count+=len(tmpDict[Arraysum[i]-k])

            if flag==1 and Arraysum[i]-k==0:
                count+=1
                flag=0
                tmpDict[Arraysum[i]-k]=[i]
                
            if Arraysum[i] in tmpDict:
                tmpDict[Arraysum[i]].append(i)
            else:
                tmpDict[Arraysum[i]]=[i]
        return count