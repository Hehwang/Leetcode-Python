class Solution:
    def compare(self,a,b):
        a,b=str(a),str(b)
        if a+b>b+a:
            return True
        else:
            return False
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=[str(x) for x in nums]
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if self.compare(nums[j],nums[j-1]):
                    nums[j-1],nums[j]=nums[j],nums[j-1]
        if nums[0][0]=='0':
            return '0'
        return ''.join(nums)  