class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count=0
        d={}
        out=[]
        for i in  range(len(A)):
            d[A[i]]=d.get(A[i],0)+1
            d[B[i]]=d.get(B[i],0)+1
            if d[A[i]]==2:
                count+=1
                d[A[i]]=0
            if d[B[i]]==2:
                count+=1
                d[B[i]]=0
            out.append(count)
        return out

