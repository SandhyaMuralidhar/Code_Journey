class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        dp={}
        for i in range(cols):
            dp[((rows-1),i)]=matrix[rows-1][i]
        
       

        for i in range(rows-2,-1,-1):
            for j in range(cols-1,-1,-1):
                
                if j-1<0:
                    val=min(dp[i+1,j],dp[i+1,j+1])
                elif j+1>cols-1:
                    val=min(dp[(i+1,j)],dp[(i+1,j-1)])
                else:
                    val=min(dp[i+1,j-1],dp[i+1,j],dp[i+1,j+1])
                dp[(i,j)]=matrix[i][j]+val
               
        min_val=float('inf')
        for i in range(cols):
            min_val=min(min_val,dp[(0,i)])
        return min_val
        