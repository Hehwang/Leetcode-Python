class Solution(object):
    def helper(self,[i,j]):
        row=1 if i<3 else (2 if i<6 else 3)
        col=1 if j<3 else (2 if j<6 else 3)
        area=(row-1)*3+col
        return [i,j,area]
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n=len(board)
        numDict={}
        for i in range(n):
            for j in range(n):
                tmp=board[i][j]
                if tmp in numDict:
                    numDict[tmp].append([i,j])
                else:
                    numDict[tmp]=[[i,j]]
        for num in numDict:
            tmp=numDict[num]
            tmp=list(map(self.helper,tmp))
            x=list(map(lambda x:x[0],tmp))
            y=list(map(lambda x:x[1],tmp))
            z=list(map(lambda x:x[2],tmp))
            if len(x)!=len(list(set(x))) or len(y)!=len(list(set(y))) or len(z)!=len(list(set(z))):
                return False
        return True