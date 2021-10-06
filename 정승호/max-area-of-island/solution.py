class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        def dfs(i,j):
            counter = 0
            if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != 1:
                return 0
            else:
                counter += 1 
                grid[i][j] = 0 
                counter += dfs(i+1,j)
                counter += dfs(i-1,j)
                counter += dfs(i,j+1)
                counter += dfs(i, j-1)
            
            return counter 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    counter = dfs(i,j)
                    answer = max(answer, counter)
                    
        return answer

