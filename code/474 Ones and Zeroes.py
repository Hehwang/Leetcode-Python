class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # this is a two costs package problem
        ml=[0]
        nl=[0]
        for i in range(len(strs)):
            tmp=collections.Counter(strs[i])
            ml.append(tmp['0'])
            nl.append(tmp['1'])
        f=[[0]*(n+1) for _ in range(m+1)]
        for k in range(1,len(strs)+1):
            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    if i>=ml[k] and j>=nl[k]:
                        f[i][j]=max(f[i][j],f[i-ml[k]][j-nl[k]]+1)
        return f[-1][-1]