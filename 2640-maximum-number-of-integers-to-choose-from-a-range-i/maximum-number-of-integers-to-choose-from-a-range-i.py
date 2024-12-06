class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        count=0
        for num in range(1,n+1):
            if self.binary_search(banned,num):
                continue
            maxSum-=num
            if maxSum<0:
                break
            count+=1

        return count

    def binary_search(self, banned, target):
        low=0
        high=len(banned)-1
        while(low<=high):
            mid=(low+high)//2
            if banned[mid]==target:
                return True
            if banned[mid]>target:
                high=mid-1 
            else:
                low=mid+1
                
        return False 