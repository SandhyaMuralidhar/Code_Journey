class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        lis=triangle
        rows=len(triangle)-1
        
        lis[rows] = triangle[rows]

        for i in range(rows-1,-1,-1):
            for j in range(len(triangle[i])):
                
                lis[i][j] = lis[i][j]+min(lis[i+1][j],lis[i+1][j+1])
       
        return lis[0][0]