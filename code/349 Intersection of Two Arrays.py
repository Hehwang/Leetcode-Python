class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1,nums2=set(nums1),set(nums2)
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        res=[]
        for i in nums1:
            if i in nums2:
                res.append(i)
        return res