class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lists=[['','I','II','III','IV','V','VI','VII','VIII','IX'],
               ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
               ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
               ['','M','MM','MMM']]
        return lists[3][num//1000]+lists[2][num%1000//100]+lists[1][num%100//10]+lists[0][num%1000%100%10]