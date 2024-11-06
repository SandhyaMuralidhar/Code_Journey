class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        binnums=[]
        onecount=[]
        for n in nums:
            binnums.append(bin(n).replace("0b",""))
        
        for val in binnums:
            onecount.append(val.count('1'))
        
        numssorted=sorted(nums)
        i=0
        while i<len(nums):
            if nums==numssorted:
                return True
            j=0
            while j<len(nums)-1 and numssorted!=nums:
                if onecount[j]==onecount[j+1] and nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                j+=1
                
            i+=1
        return False
        
        
                
