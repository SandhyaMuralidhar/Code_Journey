class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k>0:
            
            min_ele=min(nums)
            ind=nums.index(min_ele)
            nums[ind]=nums[ind]*multiplier
            
            
            k-=1
        return nums