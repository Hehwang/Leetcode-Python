class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2!=0:
            return False
        target=sum(nums)/2
        dp=[{} for _ in range(len(nums))]
        dp[0][nums[0]]=1
        for i in range(1,len(nums)):
            dp[i][nums[i]]=1
            for j in dp[i-1]:
                if j+nums[i] in dp[i]:
                    dp[i][j+nums[i]]+=dp[i-1][j]
                else:
                    dp[i][j+nums[i]]=dp[i-1][j]
                if j in dp[i]:
                    dp[i][j]+=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]        
            if target in dp[i]:
                return True
        return False
                