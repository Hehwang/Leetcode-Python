class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        #dp1 for a great than b 
        #dp2 for b great then a
        if A[0]>B[0]:
            dp1,dp2=[0],[1]
        elif A[0]<B[0]:
            dp1,dp2=[1],[0]
        else:
            dp1,dp2=[0],[0]
        for i in range(1,len(A)):
            #print(dp1,dp2)
            if min(A[i],B[i])>max(A[i-1],B[i-1]):
                tmp=min(dp1[-1],dp2[-1])
                if A[i]>B[i]:
                    dp1.append(tmp)
                    dp2.append(tmp+1)
                elif A[i]<B[i]:
                    dp1.append(tmp+1)
                    dp2.append(tmp) 
                else:
                    dp1.append(tmp)
                    dp2.append(tmp)                     
            else:
                if A[i]>max(A[i-1],B[i-1]):
                    dp1.append(dp1[-1])
                    dp2.append(dp2[-1]+1)
                else:
                    dp1.append(dp1[-1]+1)
                    dp2.append(dp2[-1])
        
        return min(dp1[-1],dp2[-1])