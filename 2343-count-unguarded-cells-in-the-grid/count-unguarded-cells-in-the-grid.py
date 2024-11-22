class Solution:
    GUARD=1
    WALL=2
    GUARDED=3
    UNGUARDED=4
    def mark_guarded (self, row, col, grid,m,n):
        for r in range(row-1,-1,-1):
            if grid[r][col]==self.WALL or grid[r][col]==self.GUARD :
                break
            grid[r][col]=self.GUARDED
        for r in range(row+1,m):
            if grid[r][col]==self.WALL or grid[r][col]==self.GUARD :
                break
            grid[r][col]=self.GUARDED
        for c in range(col-1,-1,-1):
            if grid[row][c]==self.WALL or grid[row][c]==self.GUARD :
                break
            grid[row][c]=self.GUARDED
        for c in range(col+1,n):
            if grid[row][c]==self.WALL or grid[row][c]==self.GUARD :
                break
            grid[row][c]=self.GUARDED


    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
 
        grid=[[self.UNGUARDED ]*n for _ in range(m)]
        count=0
        print(grid)
        for guard in guards:
            grid[guard[0]][guard[1]]=self.GUARD
           
        for wall in walls:
            grid[wall[0]][wall[1]]=self.WALL
        
        for guard in guards:
            self.mark_guarded(guard[0],guard[1],grid,m,n)

       
        for row in grid:
            for col in row:
                if col==self.UNGUARDED:
                    count+=1

        return count
        