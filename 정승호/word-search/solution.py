class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {}
        
        def dfs(i,j,position):
            nonlocal visited 
            
            if position == len(word):
                return True
            
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) \
                or visited.get((i,j)) or word[position] != board[i][j]:
                return False
            
            visited[(i,j)] = True
            res = dfs(i+1,j,position+1) or dfs(i,j+1,position+1) \
                    or dfs(i-1,j,position+1) or dfs(i,j-1,position+1)
            visited[(i,j)] = False
            
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
    
    
