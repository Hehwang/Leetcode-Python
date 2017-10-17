class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        """
        思路：
        
        1. 处理字符串前后的空格
        2. 处理有可能出现的正负号
        3. 处理有效数字之前出现的‘0’：‘00123’ ‘-0035’ ‘00+123’
        4. 除了以上问题以后字符串是否为空
        5. 处理溢出
        
        """
        str=str.strip()
        if str=="":return 0
        strl=[]
        count=0
        flag=0
        for  c in str:
            if c>='1' and c<='9':
                count+=1
                strl.append(c)
            elif c=='0' and count!=0:
                count+=1
                strl.append(c)
            elif c=='-' and flag==0:
                flag+=1
                strl.append(c)
            elif c=='+' and flag==0:
                flag+=1
                strl.append(c)
            elif c=='0':continue
            else:break
        str=''.join(strl)
        if str=="":return 0
       
        if str[0]!='-'and str[0]!='+'  :return int(str) if int(str)<2147483647 else 2147483647
        elif str[0]=='-' and len(str)>1 :return -int(str[1:]) if int(str[1:])<2147483648 else -2147483648
        elif str[0]=='+' and len(str)>1 :return  int(str[1:]) if int(str[1:])<2147483647 else 2147483647
        return 0