class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1=[int(x) for x in version1.split('.')]
        v2=[int(x) for x in version2.split('.')]
        while v1[-1]==0 and len(v1)>1:
            v1=v1[:-1]
        while v2[-1]==0 and len(v2)>1:
            v2=v2[:-1]
        for i in range(min(len(v1),len(v2))):
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
        return 0 if len(v1)==len(v2) else (1 if len(v1)>len(v2) else -1)
            