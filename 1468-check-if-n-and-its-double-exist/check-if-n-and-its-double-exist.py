class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i,n in enumerate(arr):
            if n*2 in arr and n!=0 :
                return True
            elif n==0 and arr.count(n)>=2:
                return True
        return False