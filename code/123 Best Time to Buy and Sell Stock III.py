class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        listA=[0]
        listB=[0]
        local_max=0
        global_max=0
        for i in range(1,len(prices)):
            local_max=max(local_max+prices[i]-prices[i-1],prices[i]-prices[i-1])
            global_max=max(global_max,local_max)
            listA.append(global_max)
        local_max=0
        global_max=0                  
        for i in range(len(prices)-1,0,-1):
            local_max=max(local_max+prices[i]-prices[i-1],prices[i]-prices[i-1])
            global_max=max(global_max,local_max)
            listB.append(global_max)
        listB.reverse()
        res=0
        for i in range(len(prices)):
            if listA[i]+listB[i]>res:
                res=listA[i]+listB[i]
        return res