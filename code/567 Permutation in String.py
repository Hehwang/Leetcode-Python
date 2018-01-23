class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length=len(s1)
        s=dict(collections.Counter(list(s1)))
        last={}
        s1=s.copy()
        i=0
        count=length
        while i<len(s2):
            #print(i,s1,count)
            if s2[i] in s1:
                if s1[s2[i]]>0:
                    s1[s2[i]]-=1
                    count-=1
                    if s2[i] not in last:
                        last[s2[i]]=i
                    i+=1
                else:
                    s1=s.copy()
                    count=length
                    tmp=s2[i]
                    i=last[s2[i]]+1
                    last={}
            else:
                s1=s.copy()
                i+=1
                count=length
            if count==0:
                return True
        return False