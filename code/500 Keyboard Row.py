class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lists=[['q','w','e','r','t','y','u','i','o','p'],
               ['a','s','d','f','g','h','j','k','l'],
               ['z','x','c','v','b','n','m']]
        new_words=[]       
        for word_ in words:
            word=word_.lower()
            for i in range(3):
                if word[0] in lists[i]:
                    mark=i  
            flag=0
            for j in range(1,len(word)):
                if word[j] not in lists[mark]:
                    flag=1
                    break
            if flag==0:
                new_words.append(word_)               
        return new_words
