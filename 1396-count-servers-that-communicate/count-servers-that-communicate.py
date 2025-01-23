class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row={}
        col={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row[i]=row.get(i,0)+1
                    col[j]=col.get(j,0)+1
        out=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if row[i]>1 or col[j]>1:
                        out+=1

        return out
