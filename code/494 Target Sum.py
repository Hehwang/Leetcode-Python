class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if (sum(nums)-S)%2!=0:
            return 0
        target=(sum(nums)+S)/2
        dp=[{} for _ in range(len(nums))]
        dp[0][nums[0]]=1
        res=0
        for i in range(1,len(nums)):
            dp[i][nums[i]]=1
            for j in dp[i-1]:
                if j+nums[i]<=target:
                    if j+nums[i] in dp[i]:
                        dp[i][j+nums[i]]+=dp[i-1][j]
                    else:
                        dp[i][j+nums[i]]=dp[i-1][j]
                if j<=target:
                    if j in dp[i]:
                        dp[i][j]+=dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j] 
        if 0 not in dp[-1]:
            dp[-1][0]=1
        else:
            dp[-1][0]+=1
        if target in dp[-1]:
            res=dp[-1][target]
        return  res