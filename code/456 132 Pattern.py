class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        second = -2**32  
        st = []         
        for num in nums[::-1]:
            if num<second:
                return True
            while st and num>st[-1]:
                second=st.pop()
            st.append(num)
        return False
            