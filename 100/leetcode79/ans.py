class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        visited=[[0]*n for x in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if (self.dfs(board,visited,i,j,0,word)):
                        return True
        return False
    
    def dfs(self,board,visited,i,j,index,word):
        if index==len(word):
            return True
        
        if (i<0 or j<0 or i==len(board) or j==len(board[0]) or visited[i][j]):
            return False
            
        if board[i][j]==word[index]:
            visited[i][j]=1
            res=False
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                res=res or self.dfs(board,visited,i+di,j+dj,index+1,word)
            
            visited[i][j]=0
            return res
            
        return False
