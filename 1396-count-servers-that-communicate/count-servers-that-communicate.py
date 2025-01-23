class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        a=set()
        row=[0]*len(grid[0])
        col=[0]*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    row[j]+=1
                    col[i]+=1
        communicable_servers_count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if row[j] > 1 or col[i] > 1:
                        communicable_servers_count += 1

        return communicable_servers_count