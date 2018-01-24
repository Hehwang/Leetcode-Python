class Solution:
    def __init__(self):
        self.step=-1
    def helper1(self,list1):
        tmp=[[list1[0],1]]
        for i in range(1,len(list1)):
            if list1[i]==tmp[-1][0]:
                tmp[-1][1]+=1
            else:
                tmp.append([list1[i],1])
        return tmp
    def helper2(self,boxes,i):
        
        if len(boxes)==0:
            return boxes
        boxes=boxes[:i]+boxes[i+1:]
        if i-1>=0 and i<len(boxes):
            if boxes[i-1][0]!=boxes[i][0]:
                return boxes
            else:
                boxes=boxes[:i-1]+[[boxes[i-1][0],boxes[i-1][1]+boxes[i][1]]]+boxes[i+1:]
                if boxes[i-1][1]<3:
                    return boxes
                else:
                    return self.helper2(boxes,i-1)
        return boxes
                    
    def helper3(self,boxes,step,hand):
        
        if len(boxes)==0:
            if self.step==-1:
                self.step=step
            else:
                self.step=min(self.step,step)
        else:
            for i in range(len(boxes)):    
                #print(boxes,hand,'#####step=%d'%self.step,i)
                if boxes[i][0] in hand and boxes[i][1]+hand[boxes[i][0]]>=3:                     
                    self.helper3(self.helper2(boxes,i),step+3-boxes[i][1],self.helper4(hand,boxes[i][0],3-boxes[i][1]))
    def helper4(self,dd,key,val):
        d=dd.copy()
        val=d[key]-val
        d.update({key:val})
        return d                 
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        hand=dict(collections.Counter(hand))
        #print(hand)
        board=self.helper1(board)
        self.helper3(board,0,hand)
        return self.step