class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m=len(grid)
        n=len(grid[0])
        num_islands=0
        def dfs( r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!="1":
                return
            grid[r][c]="0"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    num_islands+=1

        return num_islands