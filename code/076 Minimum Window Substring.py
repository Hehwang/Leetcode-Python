class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target={}
        count=len(t)
        for letter in t:
            if letter in target:
                target[letter]+=1
            else:
                target[letter]=1
        start,end=0,-1
        min_gap=len(s)+1
        gap=""
        flag=True
        while flag:       
            if count>0:
                for i in range(end+1,len(s)):
                    if s[i] in target:
                        if target[s[i]]>0:
                            count-=1
                        target[s[i]]-=1
                    if count==0:
                        end=i
                        if end==0:
                            return s[0]
                        break
                    if i==len(s)-1:
                        flag=False
            if count==0:
                for i in range(start,end+1):
                    if s[i] in target:
                        if target[s[i]]==0:
                            count+=1
                        target[s[i]]+=1
                    if count==1:
                        if end-i+1<=min_gap:
                            gap=s[i:end+1]
                            min_gap=end-i+1
                        start=i+1
                        break
                if end==len(s)-1:
                    flag=False                
        return gap 
                    