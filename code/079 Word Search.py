class Solution:
    def __init__(self):
        self.loc={}
        #self.flag=False
    def location(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.loc:
                    self.loc[board[i][j]].append((i,j))
                else:
                    self.loc[board[i][j]]=[(i,j)]
    def updatepath(self,path,position):
        tmp=path.copy()        
        tmp.add(position)
        return tmp
    def helper(self,path,word,board,position):
        #print(path,position)
        if len(path)==len(word):
            return True
        else:
            direction=[(0,-1),(0,1),(1,0),(-1,0)]
            for dire in direction:
                i,j=position[0]+dire[0],position[1]+dire[1]
                if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and ((i,j) not in path) and board[i][j]==word[len(path)]:
                    if self.helper(self.updatepath(path,(i,j)),word,board,(i,j)):
                        return True
            return False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board)==0:
            return False
        if len(word)==0:
            return True
        self.location(board)
        if word[0] not in self.loc:
            return False
        for pos in self.loc[word[0]]:
            if self.helper(set([pos]),word,board,pos):
            #if self.flag:
                return True
        return False