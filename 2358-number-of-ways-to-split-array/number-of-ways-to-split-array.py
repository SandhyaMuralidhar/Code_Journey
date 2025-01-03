class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=0
        sum2 = sum(nums)
        sum1=0
        for i in range(len(nums)-1):
            # sum1=0
            # sum2=0
            # for j in range(0,i+1):
            #     sum1+=nums[j]
            # for j in range(i+1,len(nums)):
            #     sum2+=nums[j]
            #print(sum1,sum2)
            sum1+=nums[i]
            sum2-=nums[i]
            if sum1>=sum2:
                count+=1
        return count