class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r<0 or r>len(grid)-1 or c<0 or c>len(grid[0])-1 or visited[r][c] or  grid[r][c]==0:
                return 0
            visited[r][c]=True
            return grid[r][c]+(dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1))
        
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        max_fish_count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0 and not visited[i][j]: 
                    max_fish_count=max(max_fish_count,dfs(i,j))
        return max_fish_count