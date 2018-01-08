class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        buckets = {}
        for i, v in enumerate(nums):
            bucketNum, offset = (int(v / t), 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True
            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                del buckets[nums[i - k] / t if t else nums[i - k]]
        return False   