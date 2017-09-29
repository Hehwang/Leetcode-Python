class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([x for x in list(map(lambda x,y:x-y,prices,[prices[0]]+prices[:len(prices)-1])) if x>0]) if len(prices)>0 else 0