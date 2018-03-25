class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        rows=1
        tmpwidth=0
        i=0
        while i<len(S):
            if tmpwidth+widths[ord(S[i])-97]<=100:
                tmpwidth+=widths[ord(S[i])-97]
            else:
                tmpwidth=widths[ord(S[i])-97]
                rows+=1
            i+=1
        return [rows,tmpwidth]