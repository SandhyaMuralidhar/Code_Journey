class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # row_count=len(mat[0])
        # col_count=len(mat)
        # r={}
        # c={}
        # k=0
        
        # while k<len(arr):
        #     for i in range(col_count):
        #         for j in range(row_count): 
        #             if arr[k]==mat[i][j]: 
        #                 r[i]=r.get(i,0)+1
        #                 c[j]=c.get(j,0)+1
        #                 if ((r.get(i,0)==row_count) or (c.get(j,0)==col_count)):
        #                     return k   
        #     k+=1
        # return 0
        row_count=len(mat[0])
        col_count=len(mat)
        r={}
        c={}
        freq={}
        
        for i in range(col_count):
            for j in range(row_count):
                    freq[mat[i][j]]=[i,j]
        for i in range(len(arr)):
            val=arr[i]
            r[freq[val][0]]=r.get(freq[val][0],0)+1
            c[freq[val][1]]=c.get(freq[val][1],0)+1
            if ((r.get(freq[val][0],0)==row_count) or (c.get(freq[val][1],0)==col_count)):
                return i
        return 0   


            

