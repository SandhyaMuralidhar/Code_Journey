class Solution:
    def highestPeak(self, isWater):
        rows=len(isWater)
        cols=len(isWater[0])
        inf=rows*cols
        cell_height=[[inf] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]:
                    cell_height[i][j]=0

        for i in range(rows):
            for j in range(cols):
                min_neighbor_height_diff=inf
                neighbor_row=i-1
                neighbor_col=j
                if self.is_valid_cell(neighbor_row,neighbor_col,rows,cols):
                    min_neighbor_height_diff=min(min_neighbor_height_diff,cell_height[neighbor_row][neighbor_col])
                    
                
                neighbor_row=i
                neighbor_col=j-1
                if self.is_valid_cell(neighbor_row,neighbor_col,rows,cols):
                    min_neighbor_height_diff=min(min_neighbor_height_diff,cell_height[neighbor_row][neighbor_col])
                cell_height[i][j]=min(cell_height[i][j],min_neighbor_height_diff+1)

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                min_height_diff=inf
                neighbor_row=i+1
                neighbor_col=j
                if self.is_valid_cell(neighbor_row,neighbor_col,rows,cols):
                    min_height_diff=min(min_height_diff,cell_height[neighbor_row][neighbor_col])
                    
                
                neighbor_row=i
                neighbor_col=j+1
                if self.is_valid_cell(neighbor_row,neighbor_col,rows,cols):
                    min_height_diff=min(min_height_diff,cell_height[neighbor_row][neighbor_col])
                cell_height[i][j]=min(min_height_diff+1,cell_height[i][j])
        return cell_height

    def is_valid_cell(self,r,c,rows,cols):
        return 0<=r<rows and 0<=c<cols
                
                



        