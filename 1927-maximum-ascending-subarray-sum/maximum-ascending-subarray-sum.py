class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total=0
        max_sum=0
        for i in range(0,len(nums)):
            if nums[i]>nums[i-1]:
                total+=nums[i]
            else:
                total=nums[i]
            max_sum=max(max_sum,total)
        return max_sum