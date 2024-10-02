class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        s_arr=sorted(arr)
        unique=0
        for i in range(len(arr)):
            if i==0 or s_arr[i]!=s_arr[i-1]:
                unique+=1
            d[s_arr[i]]=unique

        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr
        