class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans=collections.defaultdict(list)
        for word in strs:
            tmp=[0]*26
            for i in range(len(word)):
                tmp[ord(word[i])-ord('a')]+=1
            ans[tuple(tmp)].append(word)
        return ans.values()