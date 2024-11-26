class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        node=-1
        val=[0]*(len(grid))
        count=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                val[i]+=grid[i][j]
        
        for i in range(len(val)):
            if val[i]>0 and count<val[i]:
                node=i
                count=val[i]
                
        return node if count>0 else -1
