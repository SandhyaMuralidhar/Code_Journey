class Solution:
    def averageValue(self, nums: List[int]) -> int:
        out=0
        count=0
        for n in nums:
            if n%3==0 and n%2==0:
                out+=n
                count+=1
        return out//count if count>0 else  out