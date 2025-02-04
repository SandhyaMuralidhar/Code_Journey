class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                total+=nums[i]
            else:
                total=nums[i]
            max_sum=max(max_sum,total)
        return max_sum