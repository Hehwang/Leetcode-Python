class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res=[1]
        k=len(primes)
        index=[0]*k
        nums=[None]*k
        for _ in range(n-1):
            for i in range(k):
                nums[i]=res[index[i]]*primes[i]
            num=min(nums)
            res.append(num)
            for i in range(k):
                if num==nums[i]:
                    index[i]+=1
        return res[-1]        