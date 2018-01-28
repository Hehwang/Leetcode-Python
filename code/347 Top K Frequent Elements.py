class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d=collections.Counter(nums)
        import heapq
        a=heapq.nlargest(k,d.items(),key=lambda x :x[1])
        return list(map(lambda x:x[0],a))