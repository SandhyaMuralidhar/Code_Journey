class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n = len(matrix[0])
        lis1 = []
        out=[]
       
        for i in range(m):
            min_ele= float('inf')
            for j in range(n):
                min_ele = min(min_ele, matrix[i][j])
            
            lis1.append(min_ele)
        for j in range(n):
            max_ele = -float('inf')
            for i in range(m):
                max_ele = max(max_ele, matrix[i][j])
            
            if max_ele in lis1:
                out.append(max_ele)
        
        return out 
                


        