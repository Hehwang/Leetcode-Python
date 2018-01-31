class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=set(['a','e','i','o','u','A','E','I','O','U'])
        start,end=0,len(s)-1
        s=list(s)
        while start<end:
            if s[start] in vowels:
                if s[end] in vowels:
                    s[start],s[end]=s[end],s[start]
                    start+=1
                    end-=1
                else:
                    end-=1
            else:
                start+=1
        return ''.join(s)