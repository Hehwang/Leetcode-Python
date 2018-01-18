class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        [left,right]=[x for x in equation.split('=')]
        if left[0]!='-':
            left='+'+left
        right_s=''
        for i in range(len(right)):
            if right[i]=='+':
                right_s+='-'
            elif right[i]=='-':
                right_s+='+'
            else:
                right_s+=right[i]
        if right_s[0]!='+':
            right_s='-'+right_s
        new=left+right_s+'+'        
        num_x=0
        constant_x=0
        last=0
        print(new)
        for i in range(1,len(new)):
            if new[i]=='+' or new[i]=='-':
                tmp=new[last:i]
                print(tmp,last,i)
                if tmp[-1]=='x':
                    if len(tmp)==2:
                        if new[last]=='+':
                            num_x+=1
                        elif new[last]=='-':
                            num_x+=-1
                        else:
                            print('BULLSHIT')
                    else:
                        num_x+=int(new[last:i-1])    
                else:
                    constant_x+=int(new[last:i])
                last=i
        print(constant_x,num_x)
        if num_x==0:
            if constant_x==0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x='+str(int(-constant_x/num_x))
                    