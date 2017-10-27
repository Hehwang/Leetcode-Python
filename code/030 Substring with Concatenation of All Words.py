class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        lenws=len(words)
        lenw=len(words[0])
        
        wordsDict={}
        for word in words:
            if word in wordsDict:
                wordsDict[word]+=1
            else:
                wordsDict[word]=1
        res=[]
        for i in range(len(s)-lenws*lenw+1):
            wordsDict_c=wordsDict.copy()
            flag=True
            for j in range(i,i+lenws*lenw,lenw):
                if s[j:j+lenw] not in wordsDict_c or wordsDict_c[s[j:j+lenw]]==0:
                    flag=False
                    break
                else:
                    wordsDict_c[s[j:j+lenw]]-=1
            if flag:
                res.append(i)
        return res
            