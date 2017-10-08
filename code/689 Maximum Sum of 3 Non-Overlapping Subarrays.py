class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        tmpsum=sum(nums[:k])
        Arraysum=[tmpsum]
        for i in range(k,len(nums)):
            tmpsum+=nums[i]-nums[i-k]
            Arraysum.append(tmpsum) 
        ### creat a new list record max value of Arraysum[:i] named front_arr
        front_arr=[0]*len(Arraysum)
        ### creat a new list record max value of Arraysum[i:] named back_arr
        back_arr=[0]*len(Arraysum)        
        tmpmax1,tmpmax2=0,0
        front_index=0
        back_index=len(Arraysum)-1
        for i in range(len(Arraysum)):
            if Arraysum[i]>tmpmax1:
                tmpmax1=Arraysum[i]
                front_index=i
            if Arraysum[len(Arraysum)-1-i]>=tmpmax2:
                tmpmax2=Arraysum[len(Arraysum)-1-i]
                back_index=len(Arraysum)-1-i                
            front_arr[i]=(tmpmax1,front_index)
            back_arr[len(Arraysum)-1-i]=(tmpmax2,back_index)
        globalmax=0
        for i in range(k,len(Arraysum)-k):
            localmax=front_arr[i-k][0]+Arraysum[i]+back_arr[i+k][0]
            if localmax>globalmax:
                globalmax=localmax
                res=[front_arr[i-k][1],i,back_arr[i+k][1]]
        return res