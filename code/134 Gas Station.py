class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sumGas=0
        sumCost=0
        start=0
        tank=0
        for i in range(len(gas)):
            sumGas+=gas[i]
            sumCost+=cost[i]
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        if sumGas<sumCost:
            return -1
        else:
            return start