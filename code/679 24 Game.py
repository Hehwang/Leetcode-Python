class Solution:
    def __init__(self):
        self.lists=[]
    # 返回两个数之间所有可能的计算结果
    def op2nums(self,a,b):
        if a==0 and b==0:
            return [a+b,a-b,a*b,b-a]
        elif a==0:
            return [a+b,a-b,a*b,a/b,b-a]
        elif b==0:
            return [a+b,a-b,a*b,b/a,b-a]
        else:
            return [a+b,a-b,a*b,b/a,b-a,a/b]
    
    def op4nums(self,a,b,c,d):
        tmp1=self.op2nums(a,b)
        ## a=>b=>c=>d
        tmp2=[]
        for i in range(len(tmp1)):
            tmp2.extend(self.op2nums(tmp1[i],c))
        res=[]
        for i in range(len(tmp2)):
            res.extend(self.op2nums(tmp2[i],d))
        ##a=>b=>(c=>d)
        tmp3=self.op2nums(c,d)
        for i in range(len(tmp1)):
            for j in range(len(tmp3)):
                res.extend(self.op2nums(tmp1[i],tmp3[j]))
        return res
    
    def helper(self,list1,path):
        if len(path)==4:
            self.lists.append(path)
        else:
            for i in range(len(list1)):
                self.helper(list1[:i]+list1[i+1:],path+[list1[i]])
           
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.helper(nums,[])
        for i in self.lists:
            for num in self.op4nums(i[0],i[1],i[2],i[3]):
                if abs(num-24)<1e-7:
                    return True
        return False