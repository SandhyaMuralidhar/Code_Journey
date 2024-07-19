class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n = len(matrix[0])
        print(m,n)
        lis1 = []
        out=[]
        lis2= []
        for i in range(m):
            min_ele= float('inf')
            for j in range(n):
                min_ele = min(min_ele, matrix[i][j])
            print("min_ele",min_ele)
            lis1.append(min_ele)
        for j in range(n):
            max_ele = -float('inf')
            for i in range(m):
                max_ele = max(max_ele, matrix[i][j])
            print("max_ele",max_ele)
            if max_ele in lis1:
                out.append(max_ele)
        
        return out 
                


        