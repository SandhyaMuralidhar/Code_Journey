class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        i=0
        count=0
        s=sorted(nums)
        #print(s)
        while (i<len(nums)-1):
            j=i+1
            start=i
            while(j<len(nums) and nums[i]<nums[j]):
                i+=1
                j+=1
            i+=1
            # print(nums[start:j])
            # print(nums[start:j] in s)
            out=nums[j:]+nums[:j]
            #if nums[start:j] in s:
            if out==s:
                count+=1
            #print(count)
        return True if count<3 and count>0 else False
        