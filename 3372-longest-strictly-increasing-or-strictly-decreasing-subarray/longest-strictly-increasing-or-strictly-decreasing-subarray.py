class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count=1
        maxi=0
        i=0
        j=0
        while i<len(nums)-1:
            count=1
            j=i+1
            while(j<=len(nums)-1 and nums[i]<nums[j]):
                print("inc",nums[i],nums[j])
                i+=1
                j+=1
                count+=1
                maxi=max(maxi,count)
               
            count=1
            j=i+1
            while(j<=len(nums)-1 and nums[i]>nums[j]):
                print("dec",nums[i],nums[j])
                i+=1
                j+=1
                count+=1
                maxi=max(maxi,count)
            count=1
            j=i+1
            while(j<=len(nums)-1 and nums[i]==nums[j]):
                print("equal",nums[i],nums[j])
                i+=1
                j+=1
             
                
        maxi=max(maxi,count)
        return maxi