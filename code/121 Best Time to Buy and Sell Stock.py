class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        local_max=0        
        global_max=0
        for i in range(1,len(prices)):
            local_max=max(local_max+prices[i]-prices[i-1],prices[i]-prices[i-1])
            global_max=max(global_max,local_max)
        return global_max