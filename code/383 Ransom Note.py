class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict=dict(collections.Counter(magazine))
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine_dict and magazine_dict[ransomNote[i]]>0:
                magazine_dict[ransomNote[i]]-=1
            else:
                return False
        return True